
def escolhaPedraPapelTesoura(jogada):
    jkpon = ["pedra", "papel", "tesoura"]
    if jogada == "1":
        jogada = jkpon[0]
    elif jogada == "2":
        jogada = jkpon[1]
    elif jogada == "3":
        jogada = jkpon[2]
    return jogada

def calcularPartida(p1,p2):

    if p1 > p2:
        print()
        print("PLAYER 1 foi o VENCEDOR!")
        print(f"---------- Placar ---------- \n"
              f" Player 1 [{p1}] X [{p2}] Player 2")
    elif p2 > p1:
        print()
        print("PLAYER 2 foi o VENCEDOR!")
        print(f"---------- Placar ---------- \n"
              f" Player 1 [{p1}] X [{p2}] Player 2")
    else:
        print()
        print("A partida foi EMPATE")
        print(f"---------- Placar ---------- \n"
              f" Player 1 [{p1}] X [{p2}] Player 2")

def opcoes():
    print("[1] - pedra\n"
          "[2] - papel\n"
          "[3] - tesoura")
    
print("-------------------- JOKEMPO ----------------------")
print("----------------- O melhor de 3 -------------------")

play2 = 0
play1 = 0

for x in range(1,4):
    print()
    if x == 3:
        print("Rodada Final")
    else:
        print(f"Rodada {x}")
    print()
    opcoes()

    Player1 = input("Player 1, selecione um dos valores [1] [2] [3] para jogar: ")
    while Player1 not in ['1','2','3']:
        print("Valor invalido!")
        opcoes()
        Player1 = input("Player 1, selecione um dos valores [1] [2] [3] para jogar: ")
    jogador1 = escolhaPedraPapelTesoura(Player1)

    opcoes()

    Player2 = input("Player 2, selecione um dos valores [1] [2] [3] para jogar: ")
    while Player2 not in ['1','2','3']:
        print("Valor invalido!")
        opcoes()
        Player2 = input("Player 2, selecione um dos valores [1] [2] [3] para jogar: ")

    jogador2 = escolhaPedraPapelTesoura(Player2)

    if jogador1 == "pedra" and jogador2 == "pedra":
        print()
        print(f"Empate - Player 1: {jogador1} || Player 2: {jogador2}")
    elif jogador1 == "pedra" and jogador2 == "tesoura":
        print()
        print(f"Player 1 ganhou! - Player 1: {jogador1} || Player 2: {jogador2}")
        play1 += 1
    elif jogador1 == "pedra" and jogador2 == "papel":
        print()
        print(f"Player 2 ganhou! - Player 1: {jogador1} || Player 2: {jogador2}")
        play2 += 1
    elif jogador1 == "papel" and jogador2 == "tesoura":
        print()
        print(f"Player 2 ganhou! - Player 1: {jogador1} || Player 2: {jogador2}")
        play2 += 1
    elif jogador1 == "papel" and jogador2 == "papel":
        print()
        print(f"Empate - Player 1: {jogador1} || Player 2: {jogador2}")
    elif jogador1 == "papel" and jogador2 == "pedra":
        print()
        print(f"Player 1 ganhou! - Player 1: {jogador1} || Player 2: {jogador2}")
        play1 += 1
    elif jogador1 == "tesoura" and jogador2 == "papel":
        print()
        print(f"Player 1 ganhou! - Player 1: {jogador1} || Player 2: {jogador2}")
        play1 += 1
    elif jogador1 == "tesoura" and jogador2 == "pedra":
        print()
        print(f"Player 2 ganhou! - Player 1: {jogador1} || Player 2: {jogador2}")
        play2 += 1
    else:
        print()
        print(f"Empate - Player 1: {jogador1} || Player 2: {jogador2}")

calcularPartida(play1,play2)