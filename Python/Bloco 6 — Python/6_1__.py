# Crie uma função duracao_em_horas(minutos) que recebe uma duração em minutos e retorna a duração convertida em horas (float, com 2 casas decimais).

def duracao_em_horas(minutos):
    return(round(minutos / 60, 2))

print(duracao_em_horas(90))