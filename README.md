# Estudo de Simulação em MRLS

Projeto de simulação para avaliar o comportamento do estimador de mínimos quadrados no modelo de regressão linear simples (MRLS) em cenários clássicos e sob violações de hipóteses.

## Estrutura

- `src/`: código principal (geração de cenários, ajuste, métricas e diagnósticos).
- `outputs/tables/`: tabelas com resultados numéricos da simulação.
- `outputs/figures/`: gráficos diagnósticos e distribuições dos estimadores.
- `docs/`: documento do algoritmo e documento metodológico top-down.
- `run_study.py`: script principal de execução.
- `estudo_simulacao_colab.ipynb`: notebook único para execução no Google Colab.
- `requirements.txt`: dependências Python.

## Requisitos

- Python 3.10+ (recomendado).
- Instalação de dependências:

```bash
python -m pip install -r requirements.txt
```

## Execução

```bash
python run_study.py
```

A execução gera automaticamente:

- `outputs/tables/resumo_metricas.csv`
- `outputs/tables/resumo_compacto.csv`
- `outputs/tables/estimativas_brutas.csv`
- Gráficos de diagnóstico em `outputs/figures/`

## Desenho experimental implementado

- Cenários: 6 grupos (com subcaso 4a/4b e dois ajustes no cenário 6).
- Tamanhos amostrais: `n = 30` e `n = 100`.
- Repetições por experimento: `B = 1000`.
- Controle de aleatoriedade: semente fixa `20260506`.
- Métricas: média, viés, variância, EQM, cobertura, taxa de rejeição sob H0 e poder sob H1.

## Referências da documentação

- Algoritmo: `docs/documento_algoritmo.md`
- Metodologia top-down: `docs/documento_metodologico_top_down.md`
