# Escreva uma função viagem_valida(viagem) que recebe um dicionário de viagem (com chave "duracao") e retorna True se a duração for maior que 0, ou False caso contrário.

def viagem_valida(viagem):
    if viagem["duracao"] > 0:
        return True
    else: 
        return False

viagem_1 = {
        "duracao": 0,
        "estacao": "A",
        "cidade": "Porto Alegre"
}

viagem_2 = {
        "duracao": 5,
        "estacao": "B",
        "cidade": "Guaíba"
}

print(viagem_valida(viagem_1))

print(viagem_valida(viagem_2))
