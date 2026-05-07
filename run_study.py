from pathlib import Path

from src.config import SCENARIO_LABELS, StudyConfig
from src.simulation import run_full_study


def main() -> None:
    root_dir = Path(__file__).resolve().parent
    cfg = StudyConfig()
    summary_df, compact_df = run_full_study(cfg=cfg, root_dir=root_dir)

    print("Estudo de simulacao concluido.")
    print(f"Semente: {cfg.seed}")
    print(f"Repeticoes por experimento: {cfg.replications}")
    print("Cenarios:", ", ".join(SCENARIO_LABELS.values()))
    print()
    print("Amostra do resumo de metricas:")
    print(summary_df.head(12).to_string(index=False))
    print()
    print("Tabela compacta (primeiras linhas):")
    print(compact_df.head(12).to_string(index=False))


if __name__ == "__main__":
    main()

