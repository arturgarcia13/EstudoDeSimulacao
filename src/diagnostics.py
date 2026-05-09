from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats


def save_residuals_vs_fitted(
    fitted: np.ndarray,
    resid: np.ndarray,
    output_file: Path,
    title: str,
) -> None:
    plt.figure(figsize=(7, 4))
    plt.scatter(fitted, resid, alpha=0.6)
    plt.axhline(0.0, color="black", linestyle="--", linewidth=1)
    plt.title(title)
    plt.xlabel("Valores ajustados")
    plt.ylabel("Residuos")
    plt.tight_layout()
    plt.savefig(output_file, dpi=150)
    plt.close()


def save_qqplot(resid: np.ndarray, output_file: Path, title: str) -> None:
    plt.figure(figsize=(6, 6))
    stats.probplot(resid, dist="norm", plot=plt)
    plt.title(title)
    plt.tight_layout()
    plt.savefig(output_file, dpi=150)
    plt.close()


def save_histogram(values: np.ndarray, output_file: Path, title: str) -> None:
    plt.figure(figsize=(7, 4))
    plt.hist(values, bins=30, alpha=0.85, edgecolor="black")
    plt.title(title)
    plt.xlabel("Valor")
    plt.ylabel("Frequencia")
    plt.tight_layout()
    plt.savefig(output_file, dpi=150)
    plt.close()


def save_boxplot(values: np.ndarray, output_file: Path, title: str) -> None:
    plt.figure(figsize=(6, 4))
    plt.boxplot(values, vert=True)
    plt.title(title)
    plt.ylabel("Valor")
    plt.tight_layout()
    plt.savefig(output_file, dpi=150)
    plt.close()

def save_scatter_with_fit(
    x: np.ndarray, 
    y: np.ndarray, 
    fitted: np.ndarray, 
    output_file: Path, 
    title: str
) -> None:
    plt.figure(figsize=(7, 4))
    plt.scatter(x, y, alpha=0.5, label="Dados")
    
    # Ordenar X para que a reta de regressão seja desenhada corretamente
    sort_idx = np.argsort(x)
    plt.plot(x[sort_idx], fitted[sort_idx], color="red", linewidth=2, label="Ajuste MRLS")
    
    plt.title(title)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()
    plt.tight_layout()
    plt.savefig(output_file, dpi=150)
    plt.close()

