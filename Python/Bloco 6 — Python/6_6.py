# Escreva uma função media_duracoes(viagens) que recebe uma lista de dicionários de viagem e retorna a média das durações (dica: some tudo com um for ou sum(), e divida pela quantidade com len()).

def media_duracoes(viagens):
    duracoes = [v["duracao"] for v in viagens]
    media = sum(duracoes) / len(duracoes)
    return(media)


viagens = [
    {"duracao": 19, "estacao_inicio": "A", "estacao_fim": "Z"},
    {"duracao": 35, "estacao_inicio": "B", "estacao_fim": "X"},
    {"duracao": 90, "estacao_inicio": "C", "estacao_fim": "Y"}
    ]   

resultado = media_duracoes(viagens)

print(resultado)