# Combine tudo: escreva um programa que crie uma lista notas = [7.5, 4.0, 9.2, 5.5, 3.0, 8.8], e usando as funções/lógicas que você já sabe:

# calcule a média das notas
# crie uma list comprehension aprovados com as notas maiores ou iguais a 6.0
# imprima quantos alunos foram aprovados e a média geral

notas = [7.5, 4.0, 9.2, 5.5, 3.0, 8.8]

def media_notas(notas):
    media = sum(notas) / len(notas)
    aprovados = [n for n in notas if n >= 6.0]
    return(len(aprovados), media)

a, m = media_notas(notas)

print(f"{a} alunos aprovados, média geral de {m:.2f}.")