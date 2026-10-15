# 6.10 — Escreva um pequeno programa que combine tudo: a partir da lista viagens (do 4.2), calcule e imprima:
#   o total de viagens
#   a duração média (usando sua função do 6.6)
#   a lista de classificações (usando sua função do 6.7)

def media_duracoes(viagens):
    duracoes = [v["duracao"] for v in viagens]
    media = sum(duracoes) / len(duracoes)
    return(media)

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

viagens = [
    {"duracao": 19, "estacao_inicio": "A", "estacao_fim": "Z"},
    {"duracao": 35, "estacao_inicio": "B", "estacao_fim": "X"},
    {"duracao": 90, "estacao_inicio": "C", "estacao_fim": "Y"}
]

total = len(viagens)

media = media_duracoes(viagens)

classificacoes = classificar_lista(viagens)

print(f"O total de viagens é {total}, a média de duração é {media} e a lista de classificações é {classificacoes}.")
