from __future__ import annotations

import numpy as np

from .config import StudyConfig


def generate_x(n: int, rng: np.random.Generator, cfg: StudyConfig) -> np.ndarray:
    return rng.uniform(cfg.x_low, cfg.x_high, size=n)


def _normal_errors(n: int, rng: np.random.Generator, sigma: float) -> np.ndarray:
    return rng.normal(loc=0.0, scale=sigma, size=n)


def _heavy_tail_errors(n: int, rng: np.random.Generator, cfg: StudyConfig) -> np.ndarray:
    base = rng.standard_t(df=cfg.t_df, size=n)
    scale = cfg.sigma / np.sqrt(cfg.t_df / (cfg.t_df - 2))
    return base * scale


def _skewed_errors(n: int, rng: np.random.Generator, cfg: StudyConfig) -> np.ndarray:
    g = rng.gamma(shape=cfg.gamma_shape, scale=cfg.gamma_scale, size=n)
    g_centered = g - (cfg.gamma_shape * cfg.gamma_scale)
    g_sd = np.sqrt(cfg.gamma_shape * (cfg.gamma_scale**2))
    return (g_centered / g_sd) * cfg.sigma


def _ar1_errors(n: int, rng: np.random.Generator, cfg: StudyConfig) -> np.ndarray:
    rho = cfg.ar1_rho
    innovations_sd = cfg.sigma * np.sqrt(1 - rho**2)
    u = rng.normal(loc=0.0, scale=innovations_sd, size=n)
    eps = np.zeros(n, dtype=float)
    eps[0] = rng.normal(loc=0.0, scale=cfg.sigma)
    for i in range(1, n):
        eps[i] = rho * eps[i - 1] + u[i]
    return eps


def generate_dataset(
    scenario: str,
    n: int,
    rng: np.random.Generator,
    cfg: StudyConfig,
    beta0: float,
    beta1: float,
) -> dict[str, np.ndarray]:
    x = generate_x(n, rng, cfg)

    if scenario == "classic_normal":
        eps = _normal_errors(n, rng, cfg.sigma)
        y = beta0 + beta1 * x + eps
    elif scenario == "heavy_tails":
        eps = _heavy_tail_errors(n, rng, cfg)
        y = beta0 + beta1 * x + eps
    elif scenario == "skewed_errors":
        eps = _skewed_errors(n, rng, cfg)
        y = beta0 + beta1 * x + eps
    elif scenario == "nonzero_mean_const":
        eps = cfg.delta_const + _normal_errors(n, rng, cfg.sigma)
        y = beta0 + beta1 * x + eps
    elif scenario == "nonzero_mean_x_dep":
        eps = cfg.delta_x * x + _normal_errors(n, rng, cfg.sigma)
        y = beta0 + beta1 * x + eps
    elif scenario == "ar1_errors":
        eps = _ar1_errors(n, rng, cfg)
        y = beta0 + beta1 * x + eps
    elif scenario == "exponential_lognormal":
        eps = rng.normal(loc=0.0, scale=cfg.lognormal_sigma, size=n)
        eta = np.exp(eps)
        y = np.exp(beta0 + beta1 * x) * eta
    else:
        raise ValueError(f"Cenario desconhecido: {scenario}")

    return {"x": x, "y": y}

