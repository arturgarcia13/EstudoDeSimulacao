from dataclasses import dataclass, field


@dataclass(frozen=True)
class StudyConfig:
    seed: int = 20260506
    replications: int = 1000
    sample_sizes: list[int] = field(default_factory=lambda: [30, 100])
    alpha: float = 0.05

    beta0: float = 1.0
    beta1: float = 2.0
    sigma: float = 1.0

    x_low: float = -2.0
    x_high: float = 2.0

    t_df: int = 3
    gamma_shape: float = 2.0
    gamma_scale: float = 1.0
    delta_const: float = 1.0
    delta_x: float = 0.6
    ar1_rho: float = 0.7
    lognormal_sigma: float = 0.4


SCENARIO_LABELS = {
    "classic_normal": "C1_classico_normal",
    "heavy_tails": "C2_caudas_pesadas",
    "skewed_errors": "C3_erros_assimetricos",
    "nonzero_mean_const": "C4a_media_erro_nao_nula_constante",
    "nonzero_mean_x_dep": "C4b_media_erro_dependente_X",
    "ar1_errors": "C5_erros_correlacionados_ar1",
    "exponential_lognormal": "C6_relacao_exponencial_lognormal",
}

