# Crie uma lista nomes_estacoes = ["A", "B", "C", "D", "E"]. Usando um for, imprima cada nome precedido do seu índice na lista, no formato: "Estação 0: A". 
# Dica: pesquise a função enumerate().

nomes_estacoes = ["A", "B", "C", "D", "E"]

for indice, nome in enumerate(nomes_estacoes):
    print(f"Estação {indice}: {nome}")