# detalhes_orcamento.py

import streamlit as st

st.title("Detalhes do Cálculo do Orçamento")

service = st.selectbox("Selecione um tipo de serviço de orçamento:", ("Identidade Visual", "Software"))

def software_explicacao():
    return st.markdown(r"""
    ## Introdução

    Este documento detalha as fórmulas e os passos utilizados para calcular o orçamento final para o desenvolvimento de um software. O cálculo leva em consideração:
    - **Valor mínimo base**
    - **Custo mensal de serviço**
    - **Custos adicionais** (como banco de dados e reuniões)
    - **Ajustes percentuais** baseados em características do projeto (urgência, complexidade, tamanho e experiência da equipe, tecnologia e histórico)
    - **Margem de lucro** aplicada
    - **Ajustes para diferentes formas de pagamento** (cartão e Pix)

    Cada etapa foi pensada para refletir a complexidade e as necessidades específicas de cada projeto.

    ---

    ## 1. Custo Base

    O orçamento inicia com um valor mínimo base. Além disso, é considerado um custo de serviço por mês, multiplicado pela duração do projeto.

    - **Valor Mínimo Base:** R$ 6.435,00
    - **Custo de Serviço Mensal:** R$ 2.000,00
                
    - **Custos Adicionais:**
    - **Banco de Dados:** R$ 1.000,00 (caso seja necessário)
    - **Reuniões:** R$ 500,00 (caso sejam necessárias)

    **Fórmula do Custo Base:**

    $$
    \text{Custo Base} = \text{Valor Mínimo Base} + (\text{Custo de Serviço Mensal} \times \text{Número de Meses}) + \text{Custos Extras}
    $$

    *Exemplo:*  
    Para um projeto de 3 meses com ambos os custos extras:

    $$
    \text{Custo Base} = 6.435,00 + (2.000,00 \times 3) + 1.000,00 + 500,00
    $$

    ---

    ## 2. Ajustes Percentuais

    Após definir o custo base, são aplicados ajustes percentuais que refletem as características do projeto:

    - **Urgência:**
    - Imediato: **+10%**
    - Próximos 3 meses: **0%**
    - Em breve: **-5%**

    - **Complexidade do Projeto:**
    - Baixa: **0%**
    - Média: **+20%**
    - Alta: **+40%**

    - **Tamanho da Equipe:**
    - 1 pessoa: **0%**
    - 2-5 pessoas: **+10%**
    - 6-10 pessoas: **+20%**
    - Mais de 10 pessoas: **+30%**

    - **Experiência da Equipe:**
    - Iniciante: **+15%**
    - Intermediário: **0%**
    - Avançado: **-10%**

    - **Plataforma/Tecnologia:**
    - Web: **0%**
    - Mobile ou Desktop: **+10%**
    - Todas: **+20%**

    - **Experiência Tecnológica Anterior:**
    - Se já investiu em soluções de tecnologia: **-5%**
    - Caso contrário: **0%**

    **Fórmula para o Custo Ajustado:**

    $$
    \text{Custo Ajustado} = \text{Custo Base} \times \Bigl(1 + \sum \text{(ajustes percentuais)}\Bigr)
    $$

    *Exemplo:*  
    Se a soma dos ajustes for de 40% (ou 0.40), então:

    $$
    \text{Custo Ajustado} = \text{Custo Base} \times 1.40
    $$

    ---

    ## 3. Aplicação da Margem de Lucro

    Após os ajustes, é aplicada uma **margem de lucro mínima de 30%** sobre o custo ajustado.

    **Fórmula:**

    $$
    \text{Valor Final} = \text{Custo Ajustado} \times 1.30
    $$

    ---

    ## 4. Ajuste para Formas de Pagamento

    São calculados os valores finais para duas formas de pagamento:

    - **Pagamento com Cartão:**  
    Acrescenta-se uma taxa de **3,29%** para pagamento via cartão (até 12x sem juros).

    **Fórmula:**

    $$
    \text{Valor com Cartão} = \text{Valor Final} \times 1.0329
    $$

    - **Pagamento por Pix:**  
    Aplica-se um desconto de **10%** para pagamento via Pix.

    **Fórmula:**

    $$
    \text{Valor com Pix} = \text{Valor Final} \times 0.90
    $$

    ---

    ## Resumo Geral do Cálculo

    1. **Cálculo do Custo Base:**

    $$
    \text{Custo Base} = 6.435,00 + (2.000,00 \times \text{meses}) + \text{Custos Extras}
    $$

    2. **Aplicação dos Ajustes Percentuais:**

    $$
    \text{Custo Ajustado} = \text{Custo Base} \times \Bigl(1 + \text{(soma dos ajustes)}\Bigr)
    $$

    3. **Aplicação da Margem de Lucro:**

    $$
    \text{Valor Final} = \text{Custo Ajustado} \times 1.30
    $$

    4. **Cálculos para Formas de Pagamento:**
    - **Cartão:**
            $$ 
            \text{Valor Final} \times 1.0329
            $$
    - **Pix:** 
            $$ 
            \text{Valor Final} \times 0.90
            $$

    Cada etapa foi desenvolvida para garantir que o valor do orçamento reflita não só os custos operacionais, mas também a complexidade e as especificidades do projeto, mantendo sempre o valor mínimo estipulado e assegurando a margem de lucro desejada.

    ---

    ## Conclusão

    Este documento esclarece as bases e os cálculos utilizados para gerar o orçamento final. Através deste método, cada variável (duração, ajustes e custos extras) é considerada de forma a refletir com precisão as necessidades do projeto. Se surgirem dúvidas ou se desejar mais informações sobre algum item específico, entre em contato com o setor responsável.
    """)

def id_visual_explicacao():
    st.text("Identidade Visual" + "Em breve")


if service == "Software":
    software_explicacao()
if service == "Identidade Visual":
    id_visual_explicacao()