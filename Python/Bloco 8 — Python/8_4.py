# Dada a lista alunos = ["Ana", "Bruno", "Carla", "Diego"], use um for com enumerate para imprimir cada nome numerado a partir de 1 (não de 0), no formato "1 - Ana".

alunos = ["Ana", "Bruno", "Carla", "Diego"]

for indice, nome in enumerate(alunos):
    print(f"{indice + 1} - {nome}")