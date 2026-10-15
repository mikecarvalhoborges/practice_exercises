# Escreva uma função soma_pares(numeros) que recebe uma lista de números e retorna a soma apenas dos valores pares.

numeros = [1, 234, 3434563, 32, 98, 43, 238497]

def soma_pares(numeros):
    return(sum([p for p in numeros if p % 2 == 0]))

print(soma_pares(numeros))