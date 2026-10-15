# Crie uma lista de dicionários produtos, cada um com "nome" e "preco" (invente 4 produtos). Escreva uma função produto_mais_caro(produtos) que retorna o nome do produto com maior preço.
# Dica: reaproveite a lógica de max() com key, mas adaptada — pode usar key=lambda p: p["preco"].

produtos = [
    {"nome": "massa", "preco": 7.50}, 
    {"nome": "farinha", "preco": 10.0},
    {"nome": "ovos", "preco": 6.0},
    {"nome": "alface", "preco": 3.5}
]

def produto_mais_caro(produtos):
    mais_alto = max(produtos, key=lambda p: p["preco"])   
    return(mais_alto["nome"], mais_alto["preco"])

print(produto_mais_caro(produtos))