viagens = [
    {"duracao": 19, "estacao_inicio": "A", "estacao_fim": "Z"},
    {"duracao": 35, "estacao_inicio": "B", "estacao_fim": "X"},
    {"duracao": 90, "estacao_inicio": "C", "estacao_fim": "Y"}
]

duracoes_longas = [
    viagem["duracao"] for viagem in viagens if viagem["duracao"] > 30
]
