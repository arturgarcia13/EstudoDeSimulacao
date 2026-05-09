from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd

from .config import SCENARIO_LABELS, StudyConfig
from .diagnostics import save_boxplot, save_histogram, save_qqplot, save_residuals_vs_fitted, save_scatter_with_fit
from .metrics import build_summary_rows, rejection_rate
from .modeling import fit_ols
from .scenarios import generate_dataset, generate_x


SCENARIOS = [
    "classic_normal",
    "heavy_tails",
    "skewed_errors",
    "nonzero_mean_const",
    "nonzero_mean_x_dep",
    "ar1_errors",
    "exponential_lognormal",
]


def _fit_for_scenario(
    scenario: str,
    x: np.ndarray,
    y: np.ndarray,
    alpha: float,
    model_label: str,
) -> dict[str, np.ndarray | float | str]:
    if scenario == "exponential_lognormal" and model_label == "log_transform":
        result = fit_ols(x, np.log(y), alpha=alpha)
    else:
        result = fit_ols(x, y, alpha=alpha)
    result["model_label"] = model_label
    return result


def _collect_replications(
    scenario: str,
    n: int,
    cfg: StudyConfig,
    rng: np.random.Generator,
    beta1_generation: float,
    model_label: str,
) -> tuple[pd.DataFrame, dict[str, np.ndarray]]:
    
    rows = []
    diagnostic_sample: dict[str, np.ndarray] | None = None

    # 1. GERA O X APENAS UMA VEZ AQUI (Fora do loop!)
    x_fixed = generate_x(n, rng, cfg)

    for _ in range(cfg.replications):
        data = generate_dataset(
            scenario=scenario,
            x=x_fixed,  # 2. Passa o X fixo
            rng=rng,
            cfg=cfg,
            beta0=cfg.beta0,
            beta1=beta1_generation,
        )
        
        fit = _fit_for_scenario(
            scenario=scenario,
            x=data["x"],
            y=data["y"],
            alpha=cfg.alpha,
            model_label=model_label,
        )

        rows.append(
            {
                "beta0_hat": fit["beta0_hat"],
                "beta1_hat": fit["beta1_hat"],
                "ci_beta0_low": fit["ci_beta0_low"],
                "ci_beta0_high": fit["ci_beta0_high"],
                "ci_beta1_low": fit["ci_beta1_low"],
                "ci_beta1_high": fit["ci_beta1_high"],
                "pvalue_beta1": fit["pvalue_beta1"],
            }
        )

        if diagnostic_sample is None:
            diagnostic_sample = {
                "x": data["x"], # 3. Vamos salvar X e Y aqui para usar no gráfico de dispersão!
                "y": data["y"],
                "fitted": np.asarray(fit["fitted"]),
                "resid": np.asarray(fit["resid"]),
            }

    if diagnostic_sample is None:
        raise RuntimeError("Nenhuma amostra foi gerada para diagnostico.")

    return pd.DataFrame(rows), diagnostic_sample


def run_full_study(cfg: StudyConfig, root_dir: Path) -> tuple[pd.DataFrame, pd.DataFrame]:
    outputs_dir = root_dir / "outputs"
    tables_dir = outputs_dir / "tables"
    figures_dir = outputs_dir / "figures"
    tables_dir.mkdir(parents=True, exist_ok=True)
    figures_dir.mkdir(parents=True, exist_ok=True)

    rng = np.random.default_rng(cfg.seed)

    summary_rows: list[dict[str, float | str | int]] = []
    all_estimation_rows: list[dict[str, float | str | int]] = []

    representative_n = max(cfg.sample_sizes)

    for scenario in SCENARIOS:
        model_labels = ["original_scale"]
        if scenario == "exponential_lognormal":
            model_labels = ["original_scale", "log_transform"]

        for n in cfg.sample_sizes:
            for model_label in model_labels:
                alt_frame, diagnostic = _collect_replications(
                    scenario=scenario,
                    n=n,
                    cfg=cfg,
                    rng=rng,
                    beta1_generation=cfg.beta1,
                    model_label=model_label,
                )
                null_frame, _ = _collect_replications(
                    scenario=scenario,
                    n=n,
                    cfg=cfg,
                    rng=rng,
                    beta1_generation=0.0,
                    model_label=model_label,
                )

                size_h0 = rejection_rate(null_frame["pvalue_beta1"].to_numpy(), cfg.alpha)
                power_h1 = rejection_rate(alt_frame["pvalue_beta1"].to_numpy(), cfg.alpha)

                rows = build_summary_rows(
                    frame=alt_frame,
                    true_beta0=cfg.beta0,
                    true_beta1=cfg.beta1,
                    alpha=cfg.alpha,
                    size_h0=size_h0,
                    power_h1=power_h1,
                )
                for row in rows:
                    row["scenario"] = scenario
                    row["scenario_label"] = SCENARIO_LABELS[scenario]
                    row["n"] = n
                    row["model"] = model_label
                    summary_rows.append(row)

                aux = alt_frame.copy()
                aux["scenario"] = scenario
                aux["scenario_label"] = SCENARIO_LABELS[scenario]
                aux["n"] = n
                aux["model"] = model_label
                all_estimation_rows.extend(aux.to_dict(orient="records"))

                #if n == representative_n:
                slug = f"{SCENARIO_LABELS[scenario]}_n{n}_{model_label}"
                save_scatter_with_fit(
                    diagnostic["x"],
                    diagnostic["y"],
                    diagnostic["fitted"],
                    figures_dir / f"{slug}_scatter_fit.png",
                    f"Ajuste - {SCENARIO_LABELS[scenario]} - {model_label}"
                )
                save_residuals_vs_fitted(
                    diagnostic["fitted"],
                    diagnostic["resid"],
                    figures_dir / f"{slug}_residuos_vs_ajustados.png",
                    f"Residuos vs ajustados - {SCENARIO_LABELS[scenario]} - {model_label}",
                )
                save_qqplot(
                    diagnostic["resid"],
                    figures_dir / f"{slug}_qqplot_residuos.png",
                    f"QQ-plot residuos - {SCENARIO_LABELS[scenario]} - {model_label}",
                )
                save_histogram(
                    alt_frame["beta1_hat"].to_numpy(),
                    figures_dir / f"{slug}_hist_beta1.png",
                    f"Histograma beta1 - {SCENARIO_LABELS[scenario]} - {model_label}",
                )
                save_boxplot(
                    alt_frame["beta1_hat"].to_numpy(),
                    figures_dir / f"{slug}_boxplot_beta1.png",
                    f"Boxplot beta1 - {SCENARIO_LABELS[scenario]} - {model_label}",
                )
                # ADICIONE AQUI OS GRÁFICOS DO BETA 0
                save_histogram(
                    alt_frame["beta0_hat"].to_numpy(),
                    figures_dir / f"{slug}_hist_beta0.png",
                    f"Histograma beta0 - {SCENARIO_LABELS[scenario]} - {model_label}",
                )
                save_boxplot(
                    alt_frame["beta0_hat"].to_numpy(),
                    figures_dir / f"{slug}_boxplot_beta0.png",
                    f"Boxplot beta0 - {SCENARIO_LABELS[scenario]} - {model_label}",
                )

    summary_df = pd.DataFrame(summary_rows).sort_values(
        by=["scenario", "n", "model", "parameter"]
    )
    estimates_df = pd.DataFrame(all_estimation_rows).sort_values(
        by=["scenario", "n", "model"]
    )

    summary_df.to_csv(tables_dir / "resumo_metricas.csv", index=False)
    estimates_df.to_csv(tables_dir / "estimativas_brutas.csv", index=False)

    compact_table = summary_df[
        ["scenario_label", "n", "model", "parameter", "bias", "variance", "mse", "coverage", "size_h0", "power_h1"]
    ]
    compact_table.to_csv(tables_dir / "resumo_compacto.csv", index=False)

    return summary_df, compact_table

