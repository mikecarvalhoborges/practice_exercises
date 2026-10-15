# Crie uma função estacao_mais_frequente(contagem_estacoes) que recebe um dicionário como o do Exercício 6.3 ({"A": 3, "B": 2, ...}) e retorna a chave (estação) com o maior valor (mais visitada).
# Dica: pesquise max() com o parâmetro key.


contagem_estacoes = {"A": 3, "B": 5, "C": 8, "D": 10, "E": 15, "F": 20}

def estacao_mais_frequente(contagem_estacoes):
    campea = max(contagem_estacoes, key=contagem_estacoes.get)   
    quantidade = contagem_estacoes[campea] 
    return(campea, quantidade)

nome_estacao, vezes = estacao_mais_frequente(contagem_estacoes)

print(f"A estação mais frequente é a {nome_estacao}: {vezes} vezes")
