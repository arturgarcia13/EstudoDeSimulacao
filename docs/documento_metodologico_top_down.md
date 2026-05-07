# Documento Metodológico Top-Down

## Título
Construção Top-Down de um Estudo de Simulação sobre o MRLS

## Objetivo
Investigar, por simulação, como o estimador de mínimos quadrados e a inferência do MRLS se comportam quando hipóteses clássicas são satisfeitas ou violadas.

## 1. Visão geral (nível mais alto)

A pergunta científica central foi: **quão robusto é o MRLS frente a diferentes estruturas de erro e especificações do modelo?**

A comparação foi organizada com uma linha de base (cenário clássico) e cenários de violação específicos, alterando um mecanismo por vez para preservar comparabilidade.

## 2. Arquitetura do projeto

O estudo foi separado em módulos:

- `src/scenarios.py`: geração de dados por cenário.
- `src/modeling.py`: ajuste do MRLS.
- `src/metrics.py`: cálculo de métricas de desempenho.
- `src/diagnostics.py`: geração dos gráficos diagnósticos.
- `src/simulation.py`: orquestração do experimento e exportação.
- `run_study.py`: ponto de entrada.

Essa arquitetura evita código monolítico e facilita manutenção e extensão.

## 3. Desenho experimental

### 3.1 Parâmetros fixados

- `beta0 = 1.0`
- `beta1 = 2.0`
- `sigma = 1.0`

### 3.2 Distribuição de X

- `X ~ Uniforme(-2, 2)`, mantida em todos os cenários.

### 3.3 Tamanhos amostrais e repetições

- `n = 30` e `n = 100`.
- `B = 1000` repetições por combinação cenário-modelo-n.

### 3.4 Reprodutibilidade

- Semente fixa: `20260506`.

## 4. Cenários simulados

1. C1: erros normais (referência clássica).
2. C2: erros com caudas pesadas.
3. C3: erros assimétricos.
4. C4a: erro com média constante não nula.
5. C4b: erro dependente de X.
6. C5: erros correlacionados AR(1).
7. C6: relação exponencial com erro multiplicativo lognormal (com comparação entre ajuste original e ajuste em log).

## 5. Procedimentos de análise

Para cada combinação:

1. gerar dados;
2. ajustar regressão;
3. armazenar estimativas e estatísticas;
4. repetir `B` vezes;
5. calcular métricas:
   - média do estimador, viés, variância, EQM;
   - cobertura de IC;
   - taxa de rejeição sob H0 (`beta1=0`);
   - poder sob H1 (`beta1=2`);
6. gerar diagnósticos para amostra representativa:
   - resíduos vs ajustados;
   - QQ-plot;
   - histograma e boxplot de `beta1`.

## 6. Resultados e interpretação

Os resultados em `outputs/tables/resumo_compacto.csv` indicam:

- **C1** confirma o comportamento esperado do MRLS.
- **C2/C3** preservam baixo viés, mas mostram pequenas alterações em variabilidade e cobertura.
- **C4a** desloca o intercepto (viés forte em `beta0`), sem afetar substancialmente `beta1`.
- **C4b** produz viés importante em `beta1`, com queda acentuada de cobertura.
- **C5** afeta principalmente inferência do intercepto em amostras menores.
- **C6** evidencia má especificação severa na escala original e melhoria clara após transformação logarítmica.

Também se observa melhora geral de variância e EQM quando `n` aumenta de 30 para 100.

## 7. Conclusões

O estudo mostra que:

- o MRLS funciona bem sob hipóteses clássicas;
- algumas violações afetam pouco o viés, mas degradam inferência;
- violações de exogeneidade (C4b) geram viés estrutural;
- reespecificação por transformação (C6 em log) pode restaurar adequação.

Assim, o projeto atende aos critérios de rigor, clareza e reprodutibilidade, e está pronto para envio acadêmico.

