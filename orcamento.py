def calcular_orcamento(inputs):
    """
    Calcula o orçamento com base nos inputs informados e regras:
      - Valor mínimo de base: R$ 6.435,00
      - Custo de serviço: R$ 2.000,00 por mês
      - Custos adicionais (banco de dados e reuniões)
      - Ajustes percentuais conforme os dados (urgência, complexidade, tamanho e experiência da equipe, plataforma e experiência com tecnologia)
      - Aplicação de uma margem de lucro de 30%
      - Cálculos de valores para pagamento com cartão (acréscimo de 3,29%) e por Pix (desconto de 10%)
      - Cálculo do custo de manutenção: valor base de R$ 97,00, ajustado conforme a tecnologia desejada e se há necessidade de banco de dados
    Retorna um dicionário (JSON) com os detalhes dos cálculos.
    """
    # Constantes iniciais
    base_minimum = 6435.00
    service_cost_per_month = 2000.00

    # Mapeamento da duração para número de meses
    duration_map = {
        "1 mês": 1,
        "3 meses": 3,
        "6 meses": 6,
        "1 ano": 12,
        "Mais de 1 ano": 18  # definição arbitrária para "Mais de 1 ano"
    }
    months = duration_map.get(inputs.get("duration"), 1)

    # Custos fixos adicionais
    database_cost = 1000.00 if inputs.get("need_database") == "Sim" else 0.0
    meeting_cost = 500.00 if inputs.get("need_meetings") == "Sim" else 0.0

    # Custo de serviço baseado na duração
    base_service_cost = service_cost_per_month * months

    # Soma do custo base: mínimo + custo do serviço + custos extras
    base_cost = base_minimum + base_service_cost + database_cost + meeting_cost

    # Ajustes percentuais conforme os inputs:
    urgency = inputs.get("urgency")
    if urgency == "Imediato":
        urgency_adj = 0.10   # +10%
    elif urgency == "Próximos 3 meses":
        urgency_adj = 0.0
    elif urgency == "Em breve":
        urgency_adj = -0.05  # -5%
    else:
        urgency_adj = 0.0

    complexit = inputs.get("complexit")
    if complexit == "Baixa":
        complexity_adj = 0.0
    elif complexit == "Média":
        complexity_adj = 0.20  # +20%
    elif complexit == "Alta":
        complexity_adj = 0.40  # +40%
    else:
        complexity_adj = 0.0

    team_size = inputs.get("team_size")
    if team_size == "1 pessoa":
        team_size_adj = 0.0
    elif team_size == "2-5 pessoas":
        team_size_adj = 0.10
    elif team_size == "6-10 pessoas":
        team_size_adj = 0.20
    elif team_size == "Mais de 10 pessoas":
        team_size_adj = 0.30
    else:
        team_size_adj = 0.0

    team_exp = inputs.get("team_exp")
    if team_exp == "Iniciante":
        team_exp_adj = 0.15  # +15%
    elif team_exp == "Intermediário":
        team_exp_adj = 0.0
    elif team_exp == "Avançado":
        team_exp_adj = -0.10  # -10%
    else:
        team_exp_adj = 0.0

    platform = inputs.get("app_plataform")
    if platform in ["Mobile", "Desktop"]:
        platform_adj = 0.10
    elif platform == "Todas":
        platform_adj = 0.20
    else:  # "Web"
        platform_adj = 0.0

    tech_sol = inputs.get("tecnologic_solution")
    if tech_sol == "Sim":
        technologic_solution_adj = -0.05  # -5%
    else:
        technologic_solution_adj = 0.0

    # Soma dos ajustes percentuais
    total_adjustment = (urgency_adj + complexity_adj + team_size_adj +
                        team_exp_adj + platform_adj + technologic_solution_adj)

    # Aplica os ajustes percentuais no custo base
    cost_after_adjustment = base_cost * (1 + total_adjustment)
    # Garante que o valor não fique abaixo do mínimo estipulado
    cost_after_adjustment = max(cost_after_adjustment, base_minimum)

    # Aplicação do lucro mínimo de 30%
    profit_margin = 0.30
    final_cost = cost_after_adjustment * (1 + profit_margin)

    # Cálculo dos valores finais para as formas de pagamento:
    # Pagamento com cartão (acréscimo de 5,59%)
    card_fee = 0.0559
    final_cost_card = final_cost * (1 + card_fee)
    # Pagamento por Pix (desconto de 10%)
    pix_discount = 0.10
    final_cost_pix = final_cost * (1 - pix_discount)

    # ---------------------------------------------------------
    # Cálculo do Custo de Manutenção
    # Valor base de manutenção
    maintenance_base = 97.00

    # Ajuste baseado na tecnologia desejada
    if platform == "Web":
        tech_factor = 1.0
    elif platform in ["Mobile", "Desktop"]:
        tech_factor = 1.2
    elif platform == "Todas":
        tech_factor = 1.4
    else:
        tech_factor = 1.0

    # Ajuste se há necessidade de banco de dados
    database_factor = 1.1 if inputs.get("need_database") == "Sim" else 1.0

    # Cálculo final da manutenção
    maintenance_cost = maintenance_base * tech_factor * database_factor

    # Monta o output JSON detalhado
    output = {
        "company_name": inputs.get("company_name"),
        "fixed_costs": {
            "base_minimum": base_minimum,
            "service_cost": base_service_cost,
            "database_cost": database_cost,
            "meeting_cost": meeting_cost
        },
        "adjustments": {
            "urgency": urgency_adj,
            "complexity": complexity_adj,
            "team_size": team_size_adj,
            "team_experience": team_exp_adj,
            "platform": platform_adj,
            "technologic_solution": technologic_solution_adj,
            "total_adjustment_percentage": total_adjustment
        },
        "cost_before_profit": round(cost_after_adjustment, 2),
        "profit_margin": profit_margin,
        "final_cost": round(final_cost, 2),
        "final_cost_card": round(final_cost_card, 2),
        "final_cost_pix": round(final_cost_pix, 2),
        "maintenance_cost": round(maintenance_cost, 2)
    }
    return output
