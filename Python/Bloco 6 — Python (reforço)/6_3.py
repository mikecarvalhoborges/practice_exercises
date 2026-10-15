# Crie um dicionário contagem_estacoes = {} vazio. Depois, dada a lista visitas = ["A", "B", "A", "C", "B", "A"], use um for para contar quantas vezes cada estação aparece, guardando o resultado em contagem_estacoes (ex: {"A": 3, "B": 2, "C": 1}).

contagem_estacoes = {}

visitas = ["A", "B", "A", "C", "B", "A"]

for item in visitas:
    if item in contagem_estacoes:
        contagem_estacoes[item] += 1
    else:
        contagem_estacoes[item] = 1

print(contagem_estacoes)