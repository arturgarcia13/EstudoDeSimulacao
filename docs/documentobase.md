# 12 Trabalho - Estudo de Simulação

## 12.1 Objetivo geral

Neste trabalho, investigue, por meio de simulação, o comportamento do estimador de mínimos quadrados no modelo de regressão linear simples (MRLS) sob diferentes condições. O objetivo é compreender, de forma aplicada e crítica, em que medida o método permanece adequado quando as hipóteses do modelo são satisfeitas ou violadas.

Ao longo do trabalho, faça:
* A geração de dados sob diferentes cenários.
* O ajuste de modelos de regressão linear simples.
* A avaliação das propriedades dos estimadores.
* A análise do desempenho da inferência estatística.
* A análise gráfica dos resíduos.
* A proposição de possíveis correções do modelo.

Desenvolva o trabalho em etapas, acompanhando o conteúdo estudado ao longo da disciplina.

---

## 12.2 Estrutura geral dos cenários

Em todos os cenários, procure manter a mesma estrutura básica, alterando apenas o mecanismo gerador dos erros ou da variável resposta. Considere gerar:

* $X_{i} \sim$ distribuição escolhida.

Apenas uma vez e, definir $Y_{i}$ de acordo com cada cenário. Utilize, sempre que possível, os mesmos valores de $\beta_{0}$ e $\beta_{1}$ em todos os cenários. Isso é essencial para que as diferenças observadas sejam atribuídas ao comportamento dos erros e não a mudanças na estrutura do modelo.

### Escolha dos parâmetros

A escolha dos parâmetros é parte fundamental do trabalho, pois parâmetros inadequados podem gerar cenários pouco informativos ou difíceis de interpretar.

**Parâmetros do modelo**
Escolha valores simples e interpretáveis, por exemplo:
* $\beta_{0} \in \{0, 1, 2\}$.
* $\beta_{1} \in \{0.5, 1, 2\}$.

Evite valores muito grandes, pois podem gerar respostas em escalas pouco naturais, e evite valores muito pequenos, que dificultam a identificação da relação entre X e Y.

**Distribuição de X**
Garanta que X apresente variabilidade suficiente, uma vez que a precisão do estimador de $\beta_{1}$ depende diretamente da dispersão de X. Possibilidades adequadas incluem:
* $X_{i} \sim U(0, 10)$.
* $X_{i} \sim N(5, 2^{2})$.
* Valores fixos igualmente espaçados.

Utilize a mesma estrutura de X em todos os cenários.

**Variabilidade dos erros**
Escolha valores como $\sigma = 1$ ou $\sigma = 2$. Se a variabilidade for muito pequena, os dados se tornam quase determinísticos. Se for muito grande, o ruído pode encobrir completamente a relação entre X e Y.

**Tamanho da amostra**
Utilize pelo menos dois tamanhos amostrais, por exemplo:
* $n = 30$ e $n = 100$.

Compare os resultados entre tamanhos diferentes e observe o efeito do aumento da amostra.

**Número de repetições**
Utilize um número suficientemente grande de repetições, por exemplo:
* $B = 1000$ ou mais.

Isso é essencial para que as estimativas empíricas de viés, variância e cobertura sejam estáveis.

---

### 12.2.1 Cenários

**(i) Modelo clássico normal**
Considere:
* $Y_{i} = \beta_{0} + \beta_{1}X_{i} + \epsilon_{i}$.
* Com $\epsilon_{i} \sim \mathcal{N}(0, \sigma^{2})$.

Os erros são independentes, com média zero e variância constante. Utilize este cenário como referência e compare todos os demais resultados com ele. Espere observar, neste caso, o comportamento mais próximo da teoria clássica do MRLS.

**(ii) Erros com curtose elevada (caudas pesadas)**
Considere:
* $Y_{i} = \beta_{0} + \beta_{1}X_{i} + \epsilon_{i}$.

Com erros de média zero e distribuição com caudas mais pesadas que a normal, como uma distribuição t de Student com poucos graus de liberdade. Garanta que os erros tenham média zero. Observe a ocorrência de valores extremos, visto que em distribuições com caudas pesadas a probabilidade de observar valores muito distantes da média é maior. Avalie:
* A estabilidade dos estimadores.
* A presença de observações influentes.
* O impacto sobre intervalos de confiança e testes.

Compare sempre com o cenário normal.

**(iii) Erros com assimetria**
Considere:
* $Y_{i} = \beta_{0} + \beta_{1}X_{i} + \epsilon_{i}$.

Com erros assimétricos e média zero. Construa os erros da seguinte forma:
* Gere $U_{i}$ de uma distribuição Gamma e defina $\epsilon_{i} = U_{i} - E(U_{i})$.

Assim, os erros terão média zero, mas não serão simétricos. Observe que média zero não implica simetria nem normalidade. Avalie:
* A forma da distribuição dos estimadores.
* Possíveis distorções na inferência.
* O comportamento do QQ-plot.

**(iv) Erros com média diferente de zero**
Considere:
* $Y_{i} = \beta_{0} + \beta_{1}X_{i} + \epsilon_{i}$.
* Com $\epsilon_{i} \sim \mathcal{N}(\mu_{\epsilon}, \sigma^{2}), \mu_{\epsilon} \ne 0$.

Observe o que ocorre com o intercepto e com o coeficiente angular. Faça uma análise cuidadosa, pois quando há intercepto no modelo, uma média constante dos erros pode ser absorvida pelo intercepto. Isso significa que o impacto sobre $\beta_{1}$ pode não ser tão evidente nesse caso.
Em seguida, considere uma situação mais geral:
* $\epsilon_{i} = \delta X_{i} + u_{i}, u_{i} \sim \mathcal{N}(0, \sigma^{2})$.

Nesse caso: $E(\epsilon_{i}|X_{i}) \ne 0$. Aqui há uma violação mais forte da hipótese do modelo. Compare os dois casos e avalie:
* O impacto sobre os estimadores.
* A presença de viés.
* A validade da inferência.

**(v) Erros correlacionados**
Considere:
* $Y_{i} = \beta_{0} + \beta_{1}X_{i} + \epsilon_{i}$.
* Com erros definidos por: $\epsilon_{i} = \rho\epsilon_{i-1} + u_{i}, u_{i} \sim \mathcal{N}(0, \sigma^{2})$.

Escolha valores como $\rho = 0.5$ ou $\rho = 0.8$. Observe que os erros não são independentes. Neste cenário, o problema principal não é a média dos erros nem necessariamente sua distribuição marginal, mas a dependência entre observações. Avalie:
* A variabilidade dos estimadores.
* Os erros-padrão estimados.
* A cobertura dos intervalos de confiança.
* O comportamento dos testes.

Observe também padrões nos resíduos.

**(vi) Relação exponencial com erro multiplicativo lognormal**
Considere:
* $Y_{i} = exp(\beta_{0} + \beta_{1}X_{i})\eta_{i}$.
* Com $\eta_{i} \sim log\mathcal{N}(0, \sigma^{2})$.

Equivalentemente:
* $Y_{i} = exp(\beta_{0} + \beta_{1}X_{i} + \epsilon_{i})$, $\epsilon_{i} \sim \mathcal{N}(0, \sigma^{2})$.

Neste cenário, o modelo não é linear na escala original de Y. Ajuste inicialmente um modelo linear simples entre Y e X. Observe:
* Padrões nos resíduos.
* Possíveis desvios de linearidade.
* Comportamento da variância.

Em seguida, aplique a transformação:
* $log(Y_{i}) = \beta_{0} + \beta_{1}X_{i} + \epsilon_{i}$.

Ajuste novamente o modelo. Compare os resultados antes e depois da transformação e avalie a adequação do modelo em cada escala.

---

## 12.3 Algoritmo geral da simulação

Utilize a mesma estrutura em todos os cenários.

* **Passo 1:** Defina os parâmetros do modelo; a distribuição de X; o tamanho da amostra n; e o número de repetições B.
* **Passo 2:** Gere os valores de $X_{1}, ..., X_{n}$.
* **Passo 3:** Gere os erros ou diretamente a variável resposta Y, de acordo com o cenário.
* **Passo 4:** Ajuste o modelo: $Y_{i} = \alpha_{0} + \alpha_{1}X_{i} + e_{i}$.
* **Passo 5:** Armazene, para cada repetição: $\hat{\beta}_{0}$; $\hat{\beta}_{1}$; e demais quantidades de interesse.
* **Passo 6:** Repita o processo B vezes.
* **Passo 7:** Calcule a média dos estimadores; viés; variância; erro quadrático médio; e, se desejar, outras quantidades.
* **Passo 8:** Construa gráficos como histogramas, boxplots e QQ-plots. Analise a forma das distribuições dos estimadores.

---

## 12.4 Etapas do trabalho

**Estimação**
Repita o processo de simulação. Calcule e interprete:
* A média dos estimadores.
* O viés.
* A variância.
* O erro quadrático médio.

Compare os resultados entre cenários.

**Inferência**
Construa intervalos de confiança para $\beta_{0}$ e $\beta_{1}$. Verifique, em cada repetição, se o intervalo contém o valor verdadeiro. Calcule a cobertura e compare entre cenários.

**Testes**
Considere:
* $\beta_{1} = 0$.
* $\beta_{1} \ne 0$.

Realize testes em cada repetição. Calcule:
* A taxa de rejeição sob $H_{0}$.
* O poder do teste.

Compare os resultados.

**Diagnóstico e correção**
Para cada cenário, gere uma única amostra. Ajuste o modelo. Construa o gráfico de resíduos vs ajustados e o QQ-plot. Observe padrões e identifique violações. Proponha correções:
* Transformações.
* Reespecificação do modelo.

Compare os modelos.

---

## 12.5 Orientações e observações

* Utilize o cenário clássico como referência.
* Altere apenas um aspecto por vez.
* Observe o efeito do tamanho da amostra.
* Analise cuidadosamente o cenário com média dos erros diferente de zero.
* No caso de erros correlacionados, concentre a análise nos erros-padrão, intervalos e testes.
* No cenário exponencial, compare claramente os modelos antes e depois da transformação.

Explique com clareza:
* Como os dados foram gerados.
* Quais medidas foram utilizadas.
* O que foi observado.
* Quais conclusões podem ser tiradas sobre o comportamento do MRLS.

### Forma de entrega

Apresente o trabalho de forma clara, organizada e reproduzível. Você pode utilizar:
* Relatório em Markdown.
* Notebook (Google Colab, Jupyter).
* Documento com texto, tabelas e gráficos.

Organize o material de modo que seja possível compreender todo o processo realizado.