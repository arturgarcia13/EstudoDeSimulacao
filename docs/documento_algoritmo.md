# Documento do Algoritmo

## Título

Algoritmo de Simulação para Avaliação do MRLS sob Diferentes Condições dos Erros

## Objetivo

Implementar um algoritmo reproduzível que:

1. gere dados em múltiplos cenários;
2. ajuste modelos de regressão linear simples;
3. consolide métricas de estimação, inferência e testes;
4. produza diagnósticos gráficos automáticos.

## Entradas

- Parâmetros globais (`src/config.py`):
  - `beta0 = 1.0`, `beta1 = 2.0`, `sigma = 1.0`.
  - `n in {30, 100}`.
  - `B = 1000`.
  - `alpha = 0.05`.
  - `seed = 20260506`.
- Cenários:
  - C1: normal clássico.
  - C2: caudas pesadas (t de Student, gl=3).
  - C3: erros assimétricos (Gamma centralizada).
  - C4a: média do erro constante não nula.
  - C4b: média do erro dependente de `X`.
  - C5: erros AR(1).
  - C6: relação exponencial com erro multiplicativo lognormal.

## Saídas

- Tabelas em `outputs/tables/`:
  - `estimativas_brutas.csv`
  - `resumo_metricas.csv`
  - `resumo_compacto.csv`
- Gráficos em `outputs/figures/`:
  - resíduos vs ajustados;
  - QQ-plot de resíduos;
  - histograma de `beta1`;
  - boxplot de `beta1`.

## Fluxo de execução do algoritmo

1. O script `run_study.py` instancia `StudyConfig`.
2. A função `run_full_study` percorre todos os cenários, tamanhos amostrais e modelos.
3. Para cada combinação:
   - roda simulação sob H1 (`beta1 = 2`) para estimação/inferência/poder;
   - roda simulação sob H0 (`beta1 = 0`) para taxa de rejeição.
4. Em cada repetição:
   - gera `X`;
   - gera `Y` conforme o cenário;
   - ajusta OLS (`statsmodels.OLS`);
   - salva estimativas (`beta0_hat`, `beta1_hat`), p-valor e ICs.
5. Ao final da combinação:
   - calcula média, viés, variância, EQM;
   - calcula cobertura empírica dos ICs;
   - calcula taxa de rejeição sob H0;
   - calcula poder sob H1.
6. Para `n=100`, salva gráficos diagnósticos por cenário/modelo.
7. Exporta as tabelas finais em CSV.

## Como cada cenário é gerado

- C1: `Y = beta0 + beta1*X + e`, `e ~ N(0, sigma^2)`.
- C2: mesmo modelo, com `e ~ t(df=3)` escalado para variância comparável.
- C3: mesmo modelo, com `e` de distribuição Gamma centralizada e padronizada.
- C4a: `e = delta_const + u`, com `u ~ N(0, sigma^2)`.
- C4b: `e = delta_x*X + u`, violando `E(e|X)=0`.
- C5: `e_t = rho*e_{t-1} + u_t` (AR(1)).
- C6: `Y = exp(beta0 + beta1*X)*eta`, `eta = exp(e)`; compara ajuste na escala original e em `log(Y)`.

## Principais resultados observados (resumo objetivo)

Com base em `outputs/tables/resumo_compacto.csv`:

- **C1 (clássico)**: viés próximo de zero, cobertura próxima de 95%.
- **C2 e C3 (não normalidade/assimetria)**: viés baixo e cobertura ainda próxima de 95%, com pequenas variações.
- **C4a (média não nula constante)**: forte viés no intercepto (aprox. +1), com cobertura do intercepto próxima de zero.
- **C4b (erro dependente de X)**: forte viés no coeficiente angular (aprox. +0.60), cobertura de `beta1` muito baixa.
- **C5 (AR1)**: cobertura do intercepto reduzida (especialmente em `n=30`), mostrando efeito da dependência.
- **C6**:
  - ajuste na escala original: viés e EQM muito altos;
  - ajuste com log-transform: viés praticamente nulo e cobertura adequada.

## Conclusão

O algoritmo cumpre os objetivos de simular, estimar, comparar e diagnosticar o MRLS em todos os cenários exigidos, com reprodutibilidade e saída automática para análise e envio acadêmico.
