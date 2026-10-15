# Usando a lista de dicionários viagens (do Exercício 4.2), escreva uma list comprehension chamada estacoes_inicio que extraia apenas os valores de "estacao_inicio" de todas as viagens (sem filtro).

viagens = [
    {"duracao": 19, "estacao_inicio": "A", "estacao_fim": "Z"},
    {"duracao": 35, "estacao_inicio": "B", "estacao_fim": "X"},
    {"duracao": 90, "estacao_inicio": "C", "estacao_fim": "Y"}
]

estacoes_inicio = [v["estacao_inicio"] for v in viagens]

print(estacoes_inicio)