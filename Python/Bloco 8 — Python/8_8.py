# Escreva uma função contar_vogais(texto) que recebe uma string e retorna quantas vogais ela contém (considere só minúsculas, ou transforme o texto com .lower() antes).

def contar_vogais(texto):
    vogais = "aeiou"
    contador = 0

    for letra in texto:
        if letra in vogais:
            contador += 1

    return(contador)

texto_original = "Ola, Mundo"

texto_minusculo = texto_original.lower()

resultado = contar_vogais(texto_minusculo)

print(resultado)