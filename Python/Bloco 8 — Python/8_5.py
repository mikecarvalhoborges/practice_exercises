# Crie um dicionário estoque = {"maçã": 10, "banana": 5, "laranja": 0}. Escreva uma função itens_em_falta(estoque) que retorna uma lista com os nomes dos itens cujo valor seja igual a 0.

estoque = {"maçã": 10, "banana": 5, "laranja": 0}

def itens_em_falta(estoque):
    return[f for f, valor in estoque.items() if valor == 0]

resultado = itens_em_falta(estoque)

print(resultado)