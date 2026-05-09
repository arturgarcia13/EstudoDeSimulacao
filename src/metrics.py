from __future__ import annotations

import numpy as np
import pandas as pd


def summarize_parameter(estimates: np.ndarray, true_value: float) -> dict[str, float]:
    mean_hat = float(np.mean(estimates))
    bias = mean_hat - true_value
    variance = float(np.var(estimates, ddof=1))
    mse = float(np.mean((estimates - true_value) ** 2))
    return {
        "mean_hat": mean_hat,
        "bias": bias,
        "variance": variance,
        "mse": mse,
    }


def coverage_rate(ci_low: np.ndarray, ci_high: np.ndarray, true_value: float) -> float:
    inside = (ci_low <= true_value) & (true_value <= ci_high)
    return float(np.mean(inside))


def rejection_rate(pvalues: np.ndarray, alpha: float) -> float:
    return float(np.mean(pvalues < alpha))


def build_summary_rows(
    frame: pd.DataFrame,
    true_beta0: float,
    true_beta1: float,
    alpha: float,
    size_h0: float,
    power_h1: float,
) -> list[dict[str, float | str | int | None]]:
    
    b0 = summarize_parameter(frame["beta0_hat"].to_numpy(), true_beta0)
    b1 = summarize_parameter(frame["beta1_hat"].to_numpy(), true_beta1)

    cov_b0 = coverage_rate(
        frame["ci_beta0_low"].to_numpy(),
        frame["ci_beta0_high"].to_numpy(),
        true_beta0,
    )
    cov_b1 = coverage_rate(
        frame["ci_beta1_low"].to_numpy(),
        frame["ci_beta1_high"].to_numpy(),
        true_beta1,
    )

    return [
        {
            "parameter": "beta0",
            **b0,
            "coverage": cov_b0,
            "size_h0": None,  # Ajuste aqui
            "power_h1": None, # Ajuste aqui
            "alpha": alpha,
        },
        {
            "parameter": "beta1",
            **b1,
            "coverage": cov_b1,
            "size_h0": size_h0,
            "power_h1": power_h1,
            "alpha": alpha,
        },
    ]

