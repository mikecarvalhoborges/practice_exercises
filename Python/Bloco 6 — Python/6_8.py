# Escreva uma list comprehension que retorne apenas os dicionários (viagens inteiras, não só a duração) da lista viagens em que a duração seja maior que 30. 
# Dica de conceito: a expressão pode ser o próprio item, não precisa ser um campo específico dele.

viagens = [
     {"duracao": 19, "estacao_inicio": "A", "estacao_fim": "Z"},
     {"duracao": 35, "estacao_inicio": "B", "estacao_fim": "X"},
     {"duracao": 90, "estacao_inicio": "C", "estacao_fim": "Y"}

]

maior_que_trinta = [v for v in viagens if v["duracao"] > 30]

print(maior_que_trinta)