import streamlit as st
import orcamento as calc

st.title("📝 Geração de Orçamento")

service = st.selectbox(
    "Selecione um tipo serviço:",
    ("Identidade Visual", "Software")
)

if service == "Software":
    st.write("Preencha os campos abaixo para gerar um orçamento para o desenvolvimento de um software.")
    company_name = st.text_input("Nome da Empresa:")
    dado2 = st.selectbox("Já investiu em soluções de tecnologia antes?", ("Sim", "Não"))
    dado3 = st.selectbox("Qual o nível de urgência para iniciar esse projeto?", ("Imediato", "Próximos 3 meses", "Em breve"))
    dado4 = st.selectbox("Qual a complexidade do projeto?", ("Baixa", "Média", "Alta"))
    dado5 = st.selectbox("Qual a duração do projeto?", ("1 mês", "3 meses", "6 meses", "1 ano", "Mais de 1 ano"))
    dado6 = st.selectbox("Qual o tamanho da equipe?", ("1 pessoa", "2-5 pessoas", "6-10 pessoas", "Mais de 10 pessoas"))
    dado7 = st.selectbox("Qual a experiência da equipe?", ("Iniciante", "Intermediário", "Avançado"))
    dado8 = st.selectbox("Qual a tecnologia desejada?", ("Web", "Mobile", "Desktop", "Todas"))
    dado9 = st.selectbox("Necessidade de banco de dados?", ("Sim", "Não"))
    dado10 = st.selectbox("Necessidade de reuniões para acompanhar o projeto?", ("Sim", "Não"))

    # Agrupa os inputs em um dicionário
    inputs = {
        "company_name": company_name,
        "tecnologic_solution": dado2,
        "urgency": dado3,
        "complexit": dado4,
        "duration": dado5,
        "team_size": dado6,
        "team_exp": dado7,
        "app_plataform": dado8,
        "need_database": dado9,
        "need_meetings": dado10
    }

    if "expand" not in st.session_state:
        st.session_state.expand = False

    if st.button("Gerar Orçamento"):
        values = calc.calcular_orcamento(inputs)
        st.session_state.expand = not st.session_state.expand

        with st.expander("Detalhes do Orçamento", expanded=st.session_state.expand):
            st.markdown("## Resumo do Orçamento")
            st.markdown(f"**Empresa:** {values.get('company_name')}")
            st.markdown("### Custos Fixos")
            st.markdown(f"- **Valor Mínimo Base:** R$ {values.get('fixed_costs', {}).get('base_minimum'):.2f}")
            st.markdown(f"- **Custo do Serviço (mensal):** R$ {values.get('fixed_costs', {}).get('service_cost'):.2f} (calculado conforme a duração do projeto)")
            st.markdown(f"- **Custo com Banco de Dados:** R$ {values.get('fixed_costs', {}).get('database_cost'):.2f}")
            st.markdown(f"- **Custo com Reuniões:** R$ {values.get('fixed_costs', {}).get('meeting_cost'):.2f}")

            st.markdown("### Ajustes Percentuais Aplicados")
            st.markdown(f"- **Urgência:** {values.get('adjustments', {}).get('urgency')*100:.0f}%")
            st.markdown(f"- **Complexidade:** {values.get('adjustments', {}).get('complexity')*100:.0f}%")
            st.markdown(f"- **Tamanho da Equipe:** {values.get('adjustments', {}).get('team_size')*100:.0f}%")
            st.markdown(f"- **Experiência da Equipe:** {values.get('adjustments', {}).get('team_experience')*100:.0f}%")
            st.markdown(f"- **Tecnologia/Plataforma:** {values.get('adjustments', {}).get('platform')*100:.0f}%")
            st.markdown(f"- **Experiência Tecnológica Anterior:** {values.get('adjustments', {}).get('technologic_solution')*100:.0f}%")
            st.markdown(f"- **Ajuste Total:** {values.get('adjustments', {}).get('total_adjustment_percentage')*100:.0f}%")

            st.markdown("### Cálculos Finais")
            st.markdown(f"- **Custo Antes do Lucro:** R$ {values.get('cost_before_profit'):.2f}")
            st.markdown("- **Margem de Lucro Aplicada:** 30%")
            st.markdown(f"- **Valor Final (com lucro):** **R$ {values.get('final_cost'):.2f}**")
            st.markdown(f"- **Valor para Pagamento com Cartão (acréscimo de 3,29%):** R$ {values.get('final_cost_card'):.2f}")
            st.markdown(f"- **Valor para Pagamento por Pix (desconto de 10%):** R$ {values.get('final_cost_pix'):.2f}")

            st.markdown("---")
            st.markdown("Todos os cálculos acima foram realizados aplicando os ajustes conforme os dados informados, garantindo que o orçamento reflita a complexidade e as necessidades específicas do projeto.")

            # Botão de exportação (a funcionalidade ainda não foi implementada)
            if st.button("Exportar Orçamento"):
                st.info("A funcionalidade de exportação ainda não foi implementada.")
