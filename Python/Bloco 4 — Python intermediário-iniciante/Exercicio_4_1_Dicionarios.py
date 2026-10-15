viagem = {
    "duracao": 19,
    "estacao_inicio": "A",
    "estacao_fim": "Z"
}

def resumo_viagem(viagem):
    return(f"Viagem de {viagem['estacao_inicio']} até {viagem['estacao_fim']}, duração de {viagem['duracao']} minutos.")
    
print(resumo_viagem(viagem))