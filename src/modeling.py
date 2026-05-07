from __future__ import annotations

import numpy as np
import statsmodels.api as sm


def fit_ols(x: np.ndarray, y: np.ndarray, alpha: float) -> dict[str, np.ndarray | float]:
    X = sm.add_constant(x, has_constant="add")
    model = sm.OLS(y, X).fit()
    ci = model.conf_int(alpha=alpha)
    return {
        "beta0_hat": float(model.params[0]),
        "beta1_hat": float(model.params[1]),
        "se_beta0": float(model.bse[0]),
        "se_beta1": float(model.bse[1]),
        "pvalue_beta1": float(model.pvalues[1]),
        "ci_beta0_low": float(ci[0, 0]),
        "ci_beta0_high": float(ci[0, 1]),
        "ci_beta1_low": float(ci[1, 0]),
        "ci_beta1_high": float(ci[1, 1]),
        "fitted": np.asarray(model.fittedvalues),
        "resid": np.asarray(model.resid),
    }

