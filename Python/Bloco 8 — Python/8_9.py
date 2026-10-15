# Dada a lista de dicionários viagens (reaproveite a do Bloco 4/6), escreva uma função total_por_estacao(viagens) que retorna um dicionário contando quantas viagens começaram em cada estacao_inicio (ex: {"A": 1, "B": 1, "C": 1}).'

viagens = [
    {"duracao": 19, "estacao_inicio": "A", "estacao_fim": "Z"},
    {"duracao": 35, "estacao_inicio": "B", "estacao_fim": "X"},
    {"duracao": 90, "estacao_inicio": "C", "estacao_fim": "Y"}
]

def total_por_estacao(viagens):
    contagem_estacoes = {}

    for item in viagens:
        estacao = item["estacao_inicio"]
        contagem_estacoes[estacao] = contagem_estacoes.get(estacao, 0) + 1
        
    return(contagem_estacoes)

resultado = total_por_estacao(viagens)

print(resultado)