# Crie uma função converter_para_km(metros) que recebe uma distância em metros e retorna a distância em quilômetros (2 casas decimais).

def converter_para_km(metros):
    return(round(metros / 1000, 2))

print(converter_para_km(9000))