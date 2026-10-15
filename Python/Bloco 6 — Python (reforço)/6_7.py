 # Crie uma função classificar_lista(viagens) que recebe a lista de dicionários e retorna uma nova lista de strings, uma para cada viagem, no formato "curta", "média" ou "longa" (reaproveitando a lógica do Exercício 2.2, mas aplicada a cada item da lista).

def classificar_lista(viagens):
    dicionario = []
    for item in viagens:
        duracao = item.get('duracao', 0)

        if duracao < 15:
            classificacao = "curta"
        elif  duracao  >= 15 and duracao <= 60:
            classificacao = "média"
        else:
            classificacao = "longa"

        dicionario.append(classificacao)

    return dicionario

viagem = [
    {"duracao": 2, "estacao_inicio": "A", "estacao_fim": "Z"},
    {"duracao": 35, "estacao_inicio": "B", "estacao_fim": "X"},
    {"duracao": 90, "estacao_inicio": "C", "estacao_fim": "Y"}
]

print(classificar_lista(viagem))