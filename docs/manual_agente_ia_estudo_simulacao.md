# Manual de Instrução para um Agente de IA
## Estudo de Simulação em Regressão Linear Simples

## 1. Propósito deste manual

Este manual orienta um agente de IA a desenvolver, do zero e de forma reproduzível, um estudo de simulação sobre o comportamento do estimador de mínimos quadrados no modelo de regressão linear simples (MRLS) sob diferentes violações ou condições das hipóteses do modelo.

O resultado esperado não é apenas um código que rode. O agente deve produzir um pacote completo, pronto para envio, com:

1. O projeto completo do estudo, organizado e executável.
2. Um documento explicando o que foi feito no algoritmo.
3. Um documento explicando em detalhes, com metodologia top-down, como o projeto foi construído e quais análises foram realizadas.

O manual também serve como guia de aprendizado. Ele deve permitir que alguém entenda o que foi estudado, por que cada decisão foi tomada, como os cenários foram construídos e como interpretar os resultados.

## 2. Resultado final esperado

Ao concluir o trabalho, o agente deve entregar três artefatos principais.

### 2.1 Projeto completo preparado para envio

O projeto deve estar organizado, executável e apresentado de forma profissional. Ele deve conter, no mínimo:

- Código fonte da simulação.
- Rotinas de geração de dados para cada cenário.
- Rotinas de ajuste do modelo.
- Rotinas de cálculo das métricas de estimação, inferência e testes.
- Rotinas de diagnóstico gráfico.
- Gráficos gerados automaticamente.
- Tabelas-resumo com os resultados.
- Um arquivo de instruções de execução.
- Um arquivo de dependências, se aplicável.

O projeto precisa permitir reprodução dos resultados com o mínimo de intervenção manual.

### 2.2 Documento sobre o algoritmo

Deve haver um documento específico explicando o algoritmo implementado. Esse texto precisa responder, de forma objetiva e completa:

- O que o algoritmo faz.
- Quais são as entradas.
- Quais são as saídas.
- Como cada cenário é gerado.
- Como os laços de simulação funcionam.
- Como os estimadores são armazenados e resumidos.
- Como são calculados viés, variância, erro quadrático médio e cobertura.
- Como os gráficos são produzidos.

Esse documento deve ser técnico, porém compreensível.

### 2.3 Documento metodológico top-down

O segundo documento deve ser uma explicação detalhada, em metodologia top-down, de como o projeto foi concebido e executado. Esse texto deve guiar o leitor do geral para o específico:

- Primeiro, o objetivo do estudo.
- Depois, a estrutura experimental.
- Em seguida, os cenários simulados.
- Depois, os procedimentos de análise.
- Por fim, os resultados e interpretações.

Esse documento deve ser suficientemente detalhado para que o leitor consiga aprender o processo completo e reproduzir a lógica do estudo.

## 3. Objetivo científico do estudo

O estudo deve investigar o comportamento do estimador de mínimos quadrados no MRLS quando diferentes hipóteses do modelo são satisfeitas ou violadas.

O agente deve tratar os seguintes pontos como núcleo do trabalho:

- Estimar os parâmetros do modelo sob diferentes mecanismos geradores de erro.
- Comparar o desempenho do estimador entre cenários.
- Avaliar viés, variância, erro quadrático médio e cobertura de intervalos.
- Verificar o comportamento dos testes de hipóteses.
- Observar o padrão dos resíduos e o efeito de transformações.
- Comparar o modelo original com modelos corrigidos ou reespecificados.

## 4. Princípios de execução do projeto

O agente deve seguir quatro princípios centrais.

### 4.1 Reprodutibilidade

Toda simulação deve poder ser repetida com os mesmos resultados, desde que a semente aleatória seja mantida.

### 4.2 Comparabilidade

Os cenários devem ser comparados com a mesma base estrutural sempre que possível. A ideia é alterar apenas um elemento por vez para isolar o efeito da violação estudada.

### 4.3 Clareza analítica

Os resultados não devem ser apenas calculados. Eles precisam ser interpretados com foco em:

- O que mudou.
- Por que mudou.
- O que isso significa para o MRLS.

### 4.4 Organização didática

O produto final deve ser útil para envio acadêmico e também para estudo pessoal. Isso exige texto claro, seções bem separadas, figuras legíveis e uma explicação lógica do processo.

## 5. Estrutura conceitual do estudo

O documento-base define um conjunto de cenários que o agente deve implementar. A estrutura geral deve ser mantida em todos eles:

- Gerar a variável explicativa X.
- Gerar os erros ou a variável resposta Y conforme o cenário.
- Ajustar o MRLS.
- Armazenar os estimadores e estatísticas de interesse.
- Repetir o processo muitas vezes.
- Resumir os resultados.
- Produzir gráficos e interpretações.

## 6. Cenários que devem ser contemplados

O agente deve desenvolver, no mínimo, os seguintes cenários.

### 6.1 Cenário 1: modelo clássico normal

Modelo de referência:

- Y_i = β_0 + β_1 X_i + ε_i
- ε_i ~ N(0, σ²)

Este cenário deve funcionar como linha de base para comparação com todos os demais.

O agente deve usar esse cenário para verificar o comportamento esperado sob as hipóteses clássicas do MRLS.

### 6.2 Cenário 2: erros com caudas pesadas

Os erros devem ter média zero, mas distribuição com curtose elevada, por exemplo uma distribuição t de Student com poucos graus de liberdade.

O objetivo é observar:

- Sensibilidade a valores extremos.
- Estabilidade dos estimadores.
- Efeito sobre intervalos de confiança.
- Efeito sobre testes.

### 6.3 Cenário 3: erros assimétricos

Os erros devem ter média zero, mas não ser simétricos. Uma forma adequada é gerar uma variável Gamma e centralizá-la subtraindo sua esperança.

O objetivo é avaliar:

- Forma empírica da distribuição dos estimadores.
- Possíveis distorções inferenciais.
- Comportamento dos QQ-plots.

### 6.4 Cenário 4: erros com média diferente de zero

O agente deve distinguir dois subcasos:

- Erros com média constante diferente de zero.
- Erros com dependência de X, por exemplo ε_i = δ X_i + u_i.

O segundo subcaso é mais forte, pois viola a condição E(ε_i | X_i) = 0.

O objetivo é observar:

- O impacto sobre o intercepto.
- O impacto sobre o coeficiente angular.
- A presença de viés.
- A validade da inferência.

### 6.5 Cenário 5: erros correlacionados

Os erros devem seguir uma estrutura dependente, por exemplo um processo autoregressivo de primeira ordem:

- ε_i = ρ ε_{i-1} + u_i

O estudo deve observar:

- Efeito sobre os erros-padrão.
- Cobertura de intervalos.
- Comportamento dos testes.
- Padrões nos resíduos.

### 6.6 Cenário 6: relação exponencial com erro multiplicativo lognormal

A variável resposta deve seguir uma relação multiplicativa:

- Y_i = exp(β_0 + β_1 X_i) η_i

ou, equivalentemente, uma relação log-linear:

- log(Y_i) = β_0 + β_1 X_i + ε_i

O agente deve comparar:

- Ajuste na escala original.
- Ajuste após transformação logarítmica.
- Padrões nos resíduos.
- Melhor adequação do modelo transformado.

## 7. Especificação experimental mínima

O agente deve definir, de forma explícita, os seguintes elementos experimentais.

### 7.1 Parâmetros do modelo

O manual-base sugere valores simples. O agente deve priorizar interpretação fácil.

Sugestão:

- β_0 em valores pequenos e interpretáveis.
- β_1 em valores positivos e claramente distintos de zero.

### 7.2 Distribuição de X

X deve apresentar variabilidade suficiente para permitir boa estimação do coeficiente angular.

O agente pode escolher, por exemplo:

- Uniforme em intervalo moderado.
- Normal com média central e variância controlada.
- Valores igualmente espaçados.

A mesma estrutura para X deve ser mantida entre cenários, salvo justificativa explícita.

### 7.3 Tamanhos amostrais

Devem ser usados pelo menos dois tamanhos amostrais.

Exemplo:

- n pequeno, como 30.
- n maior, como 100.

A comparação entre eles é obrigatória para mostrar o efeito do aumento da amostra.

### 7.4 Número de repetições

O número de repetições deve ser grande o suficiente para estabilidade empírica.

Recomendação mínima:

- B = 1000 ou mais.

Se o agente perceber que a variabilidade das métricas continua alta, deve aumentar B.

### 7.5 Semente aleatória

Deve existir um controle de aleatoriedade.

O agente deve registrar a semente usada e, se possível, permitir reprodução por configuração.

## 8. Métricas que o projeto deve calcular

O agente deve implementar um conjunto completo de métricas.

### 8.1 Métricas de estimação

Para cada parâmetro estimado, o projeto deve calcular:

- Média dos estimadores.
- Viés.
- Variância.
- Erro quadrático médio.

### 8.2 Métricas de inferência

O projeto deve construir intervalos de confiança para β_0 e β_1 e calcular cobertura empírica.

### 8.3 Métricas de testes

O projeto deve avaliar:

- Taxa de rejeição sob a hipótese nula.
- Poder do teste sob a hipótese alternativa.

### 8.4 Métricas diagnósticas

O projeto deve produzir e interpretar, pelo menos:

- Resíduos versus ajustados.
- QQ-plot dos resíduos.
- Histogramas das distribuições dos estimadores.
- Boxplots dos estimadores ou das medidas de interesse.

## 9. Metodologia top-down para construção do projeto

Esta é a parte mais importante para orientar o agente.

A metodologia top-down significa construir a solução do geral para o específico, e não o contrário.

### 9.1 Nível 1: definir o objetivo geral

Antes de codificar qualquer coisa, o agente deve responder:

- Qual pergunta científica está sendo feita?
- O que deve ser comparado?
- Quais hipóteses do MRLS serão testadas por simulação?

A resposta deve ser transformada em um enunciado claro do estudo.

### 9.2 Nível 2: definir a arquitetura do projeto

Em seguida, o agente deve planejar a estrutura do projeto como um sistema dividido em partes.

A arquitetura deve conter, no mínimo:

- Módulo de geração de dados.
- Módulo de ajuste do modelo.
- Módulo de extração de resultados.
- Módulo de cálculo de métricas.
- Módulo de gráficos.
- Módulo de relatórios.

Essa divisão evita código monolítico e facilita manutenção.

### 9.3 Nível 3: definir o desenho experimental

Depois da arquitetura, o agente deve estabelecer o experimento de simulação:

- Cenários.
- Tamanhos amostrais.
- Número de repetições.
- Parâmetros.
- Critérios de comparação.

Esse desenho deve ser descrito antes da implementação, para não haver decisões arbitrárias durante a codificação.

### 9.4 Nível 4: implementar o núcleo da simulação

O núcleo deve seguir uma lógica simples:

1. Gerar X.
2. Gerar erros ou Y.
3. Ajustar regressão.
4. Salvar estimativas e estatísticas.
5. Repetir B vezes.

O agente deve testar o núcleo em um único cenário antes de expandir para os demais.

### 9.5 Nível 5: implementar as rotinas de resumo

Depois do núcleo funcionando, o agente deve construir as funções de resumo.

Essas funções devem calcular:

- Média.
- Viés.
- Variância.
- Erro quadrático médio.
- Cobertura.
- Taxa de rejeição.
- Poder.

Isso separa simulação de pós-processamento.

### 9.6 Nível 6: implementar os diagnósticos

O agente deve então criar os diagnósticos gráficos para uma amostra representativa em cada cenário.

Essa etapa deve responder:

- O modelo está bem especificado?
- Há sinal de não linearidade?
- Há heterocedasticidade?
- Há assimetria ou caudas pesadas?
- A transformação proposta melhora o ajuste?

### 9.7 Nível 7: produzir os documentos finais

Com o código validado, o agente deve escrever os textos finais.

Primeiro, o documento do algoritmo, explicando o funcionamento computacional.

Depois, o documento metodológico top-down, explicando a lógica científica e analítica do projeto.

## 10. Sequência recomendada de implementação

O agente deve seguir esta ordem prática.

### 10.1 Planejamento

- Ler o documento-base.
- Identificar os cenários.
- Fixar parâmetros e critérios.
- Definir a linguagem e bibliotecas.
- Definir a estrutura de pastas.

### 10.2 Protótipo mínimo

- Implementar um cenário simples.
- Rodar uma simulação curta.
- Conferir se os estimadores saem como esperado.

### 10.3 Expansão

- Adicionar os demais cenários.
- Adicionar diferentes tamanhos amostrais.
- Adicionar métricas de inferência e testes.

### 10.4 Diagnóstico

- Gerar gráficos por cenário.
- Identificar padrões de resíduos.
- Avaliar se as correções propostas fazem sentido.

### 10.5 Consolidação

- Organizar resultados em tabelas.
- Redigir os textos explicativos.
- Revisar nomenclatura, coerência e apresentação.

## 11. Estrutura sugerida do projeto final

O agente deve organizar o projeto em uma estrutura clara.

Sugestão de pastas:

- src: código principal.
- data: dados simulados ou intermediários.
- outputs: tabelas e gráficos.
- docs: documentos explicativos.
- notebooks: análises interativas, se houver.
- README: instruções gerais.

Se o agente usar notebook, o notebook deve ser limpo e bem comentado, não apenas um histórico de execução.

## 12. Conteúdo esperado do documento do algoritmo

Este documento deve explicar o mecanismo computacional do projeto. Ele precisa incluir:

- Objetivo do algoritmo.
- Entrada de dados e parâmetros.
- Fluxo de execução.
- Repetição por cenário.
- Armazenamento das estimativas.
- Cálculo das estatísticas.
- Saída final em tabelas e gráficos.

O leitor deve conseguir entender exatamente como a simulação funciona do ponto de vista operacional.

## 13. Conteúdo esperado do documento metodológico top-down

Este documento deve ser mais narrativo e analítico.

Ele deve explicar:

- Qual foi a pergunta de pesquisa.
- Como o experimento foi desenhado.
- Por que cada cenário foi escolhido.
- Como os resultados foram avaliados.
- O que foi observado em cada caso.
- Como interpretar as diferenças entre cenários.
- Quais conclusões podem ser tiradas sobre o MRLS.

O texto deve sair do geral para o específico, com progressão lógica.

## 14. Análises que o agente deve realizar

O estudo não deve se limitar a gerar números. O agente precisa interpretar os resultados.

### 14.1 Comparação entre cenários

Comparar sempre o cenário clássico com os demais.

### 14.2 Efeito do tamanho amostral

Verificar como a amostra maior altera:

- Viés.
- Variância.
- Cobertura.
- Distribuição empírica dos estimadores.

### 14.3 Efeito de violação de hipótese

Explicar como cada violação afeta o modelo:

- Não normalidade.
- Assimetria.
- Média não nula.
- Dependência serial.
- Não linearidade.

### 14.4 Efeito de transformação

No cenário exponencial, discutir claramente se a transformação logarítmica melhora o ajuste.

### 14.5 Diagnóstico de resíduos

Interpretar os gráficos para identificar:

- Linearidade.
- Homocedasticidade.
- Simetria.
- Valores extremos.
- Dependência.

## 15. Critérios de qualidade do resultado final

O agente só deve considerar o trabalho concluído quando todos os itens abaixo estiverem atendidos.

- O projeto executa sem erros relevantes.
- Os cenários estão implementados de forma consistente.
- As métricas são calculadas corretamente.
- Os gráficos são gerados e legíveis.
- Os documentos explicam bem o que foi feito.
- A linguagem está clara e coerente.
- O material final está pronto para envio.

## 16. Como o agente deve escrever os relatórios

### 16.1 Estilo

Os relatórios devem ser formais, claros e didáticos.

### 16.2 Estrutura

Cada relatório deve conter:

- Título.
- Objetivo.
- Metodologia.
- Implementação ou análise.
- Resultados.
- Conclusões.

### 16.3 Nível de detalhe

O nível de detalhe deve ser alto o suficiente para que um aluno consiga estudar o material e refazer a análise sozinho.

## 17. Recomendação de interpretação dos resultados

O agente deve evitar conclusões automáticas. Em vez disso, deve interpretar os achados no contexto do MRLS.

Exemplos de interpretação esperada:

- Em cenários com erros normais, os resultados devem se aproximar da teoria.
- Em caudas pesadas, o estimador pode continuar razoável, mas a variabilidade pode aumentar.
- Em assimetria, a forma empírica pode se desviar da normalidade.
- Em dependência serial, erros-padrão e cobertura podem ser afetados.
- Em média condicional não nula, pode surgir viés e perda de validade inferencial.
- Em relações exponenciais, a transformação logarítmica pode melhorar a adequação.

## 18. Fluxo final de entrega

O agente deve entregar o material nesta ordem lógica:

1. Projeto completo organizado.
2. Documento do algoritmo.
3. Documento metodológico top-down.
4. Verificação final de execução e consistência.

## 19. Observação final para o agente

O agente deve trabalhar como se estivesse produzindo um estudo acadêmico sério, com foco em clareza, rigor e reprodutibilidade.

A regra principal é simples:

- Primeiro entender o problema.
- Depois desenhar a solução.
- Depois implementar.
- Depois validar.
- Depois explicar.

Se esse fluxo for seguido, o resultado final será um projeto completo, didático e pronto para envio.
