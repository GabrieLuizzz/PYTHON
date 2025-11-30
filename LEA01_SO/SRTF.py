# Algoritmo SRTF(Shortest Remaining Time First)
# Formato do processo: [id, chegada, duracao, prioridade]

def srtf(processos):

    n = len(processos)

    # Índice 2 = duração
    tempo_restante = [process[2] for process in processos]

    # Vetor para marcar se o processo terminou
    concluido = [False] * n

    tempo_atual = 0
    processos_concluidos = 0

    # Armazena quando cada processo termina
    tempo_finaliza = [0] * n

    # Armazena o diagrama
    diagrama = []

    while processos_concluidos < n:

        menor_tempo = float('inf')
        processo_escolhido = -1

        # Procura o processo com menor tempo restante, que já chegou
        for i in range(n):
            chegada = processos[i][1]

            if chegada <= tempo_atual and not concluido[i] and tempo_restante[i] < menor_tempo:
                menor_tempo = tempo_restante[i]
                processo_escolhido = i

        # Se não há processo disponível
        if processo_escolhido == -1:
            diagrama.append("...")
            tempo_atual += 1
            continue

        # Executa o processo por 1 unidade de tempo
        tempo_restante[processo_escolhido] -= 1
        diagrama.append(f"P{processos[processo_escolhido][0]}")

        # Se o processo terminou
        if tempo_restante[processo_escolhido] == 0:
            concluido[processo_escolhido] = True
            processos_concluidos += 1
            tempo_finaliza[processo_escolhido] = tempo_atual + 1

        tempo_atual += 1

    # calculando tempo de vida e tempo de espera
    tempo_vida = []
    tempo_espera = []

    for i in range(n):
        chegada = processos[i][1]
        duracao = processos[i][2]

        vida = tempo_finaliza[i] - chegada
        espera = vida - duracao

        tempo_vida.append(vida)
        tempo_espera.append(espera)

    media_vida = sum(tempo_vida) / n
    media_espera = sum(tempo_espera) / n

    return diagrama, tempo_vida, tempo_espera, media_vida, media_espera

qtd = int(input("Digite o numero de processos: "))

processos = []

for i in range(qtd):
    chegada, duracao, prioridade = map(int, input(f"Digite os dados do P{i+1} (chegada, duração, prioridade): ").split())
    processos.append([i+1, chegada, duracao, prioridade])

diagrama, tempo_vida, tempo_espera, media_vida, media_espera = srtf(processos)


print("\nDIAGRAMA:")
for tempo, proc in enumerate(diagrama):
    print(f"{tempo}: {proc}")

print("\nTEMPO DE VIDA:")
for i, t in enumerate(tempo_vida):
    print(f"P{i+1} = {t}")

print("\nTEMPO DE ESPERA:")
for i, t in enumerate(tempo_espera):
    print(f"P{i+1} = {t}")

print(f"\nTempo médio de vida: {media_vida:.2f}")
print(f"Tempo médio de espera: {media_espera:.2f}")
