def classificar_viagem(duracao):
    if duracao < 15:
        return "curta"
    elif duracao >= 15 and duracao <= 60:
        return "média"
    else:
        return "longa"

tempo_um = 10
tempo_dois = 40
tempo_tres = 90

resultado_um = classificar_viagem(tempo_um)
resultado_dois = classificar_viagem(tempo_dois)
resultado_tres = classificar_viagem(tempo_tres)

print(f"A viagem de {tempo_um} minutos é {resultado_um}.")
print(f"A viagem de {tempo_dois} minutos é {resultado_dois}.")
print(f"A viagem de {tempo_tres} minutos é {resultado_tres}.")

