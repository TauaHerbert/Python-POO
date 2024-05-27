from colorama import Fore
def carregarJogo(campo):
    for x in range(0,3):
        for y in range(0,3):
            print(f"    |{campo[x][y]:^1}|",end="")
        print()
    print()
def exibirResltadoPlayer1(campo):
    if campo[0][0] == Fore.BLUE+"\033[1mX\033[0m" and campo[0][1] == Fore.BLUE+"\033[1mX\033[0m" and campo[0][2] == Fore.BLUE+"\033[1mX\033[0m":
        campo[1][0] = "'"
        campo[1][1] = "'"
        campo[1][2] = "'"
        campo[2][0] = "'"
        campo[2][1] = "'"
        campo[2][2] = "'"
        carregarJogo(campo)
    elif campo[1][0] == Fore.BLUE+"\033[1mX\033[0m" and campo[1][1] == Fore.BLUE+"\033[1mX\033[0m" and campo[1][2] == Fore.BLUE+"\033[1mX\033[0m":
        campo[0][0] = "'"
        campo[0][1] = "'"
        campo[0][2] = "'"
        campo[2][0] = "'"
        campo[2][1] = "'"
        campo[2][2] = "'"
        carregarJogo(campo)
    elif campo[2][0] == Fore.BLUE+"\033[1mX\033[0m" and campo[2][1] == Fore.BLUE+"\033[1mX\033[0m" and campo[2][2] == Fore.BLUE+"\033[1mX\033[0m":
        campo[0][0] = "'"
        campo[0][1] = "'"
        campo[0][2] = "'"
        campo[1][0] = "'"
        campo[1][1] = "'"
        campo[1][2] = "'"
        carregarJogo(campo)
    elif campo[0][0] == Fore.BLUE+"\033[1mX\033[0m" and campo[1][0] == Fore.BLUE+"\033[1mX\033[0m" and campo[2][0] == Fore.BLUE+"\033[1mX\033[0m":
        campo[0][1] = "'"
        campo[0][2] = "'"
        campo[1][1] = "'"
        campo[1][2] = "'"
        campo[2][1] = "'"
        campo[2][2] = "'"
        carregarJogo(campo)
    elif campo[0][1] == Fore.BLUE+"\033[1mX\033[0m" and campo[1][1] == Fore.BLUE+"\033[1mX\033[0m" and campo[2][1] == Fore.BLUE+"\033[1mX\033[0m":
        campo[0][0] = "'"
        campo[0][2] = "'"
        campo[1][0] = "'"
        campo[1][2] = "'"
        campo[2][0] = "'"
        campo[2][2] = "'"
        carregarJogo(campo)
    elif campo[0][2] == Fore.BLUE+"\033[1mX\033[0m" and campo[1][2] == Fore.BLUE+"\033[1mX\033[0m" and campo[2][2] == Fore.BLUE+"\033[1mX\033[0m":
        campo[0][0] = "'"
        campo[0][1] = "'"
        campo[1][0] = "'"
        campo[1][1] = "'"
        campo[2][0] = "'"
        campo[2][1] = "'"
        carregarJogo(campo)
    elif campo[0][0] == Fore.BLUE+"\033[1mX\033[0m" and campo[1][1] == Fore.BLUE+"\033[1mX\033[0m" and campo[2][2] == Fore.BLUE+"\033[1mX\033[0m":
        campo[0][1] = "'"
        campo[0][2] = "'"
        campo[1][0] = "'"
        campo[1][2] = "'"
        campo[2][0] = "'"
        campo[2][1] = "'"
        carregarJogo(campo)
    elif campo[0][2] == Fore.BLUE+"\033[1mX\033[0m" and campo[1][1] == Fore.BLUE+"\033[1mX\033[0m" and campo[2][0] == Fore.BLUE+"\033[1mX\033[0m":
        campo[0][0] = "'"
        campo[0][1] = "'"
        campo[1][0] = "'"
        campo[1][2] = "'"
        campo[2][1] = "'"
        campo[2][2] = "'"
        carregarJogo(campo)
def exibirResltadoPlayer2(campo):
    if campo[0][0] == Fore.RED+"\033[1mO\033[0m" and campo[0][1] == Fore.RED+"\033[1mO\033[0m" and campo[0][2] == Fore.RED+"\033[1mO\033[0m":
        campo[1][0] = "'"
        campo[1][1] = "'"
        campo[1][2] = "'"
        campo[2][0] = "'"
        campo[2][1] = "'"
        campo[2][2] = "'"
        carregarJogo(campo)
    elif campo[1][0] == Fore.RED+"\033[1mO\033[0m" and campo[1][1] == Fore.RED+"\033[1mO\033[0m" and campo[1][2] == Fore.RED+"\033[1mO\033[0m":
        campo[0][0] = "'"
        campo[0][1] = "'"
        campo[0][2] = "'"
        campo[2][0] = "'"
        campo[2][1] = "'"
        campo[2][2] = "'"
        carregarJogo(campo)
    elif campo[2][0] == Fore.RED+"\033[1mO\033[0m" and campo[2][1] == Fore.RED+"\033[1mO\033[0m" and campo[2][2] == Fore.RED+"\033[1mO\033[0m":
        campo[0][0] = "'"
        campo[0][1] = "'"
        campo[0][2] = "'"
        campo[1][0] = "'"
        campo[1][1] = "'"
        campo[1][2] = "'"
        carregarJogo(campo)
    elif campo[0][0] == Fore.RED+"\033[1mO\033[0m" and campo[1][0] == Fore.RED+"\033[1mO\033[0m" and campo[2][0] == Fore.RED+"\033[1mO\033[0m":
        campo[0][1] = "'"
        campo[0][2] = "'"
        campo[1][1] = "'"
        campo[1][2] = "'"
        campo[2][1] = "'"
        campo[2][2] = "'"
        carregarJogo(campo)
    elif campo[0][1] == Fore.RED+"\033[1mO\033[0m" and campo[1][1] == Fore.RED+"\033[1mO\033[0m" and campo[2][1] == Fore.RED+"\033[1mO\033[0m":
        campo[0][0] = "'"
        campo[0][2] = "'"
        campo[1][0] = "'"
        campo[1][2] = "'"
        campo[2][0] = "'"
        campo[2][2] = "'"
        carregarJogo(campo)
    elif campo[0][2] == Fore.RED+"\033[1mO\033[0m" and campo[1][2] == Fore.RED+"\033[1mO\033[0m" and campo[2][2] == Fore.RED+"\033[1mO\033[0m":
        campo[0][0] = "'"
        campo[0][1] = "'"
        campo[1][0] = "'"
        campo[1][1] = "'"
        campo[2][0] = "'"
        campo[2][1] = "'"
        carregarJogo(campo)
    elif campo[0][0] == Fore.RED+"\033[1mO\033[0m" and campo[1][1] == Fore.RED+"\033[1mO\033[0m" and campo[2][2] == Fore.RED+"\033[1mO\033[0m":
        campo[0][1] = "'"
        campo[0][2] = "'"
        campo[1][0] = "'"
        campo[1][2] = "'"
        campo[2][0] = "'"
        campo[2][1] = "'"
        carregarJogo(campo)
    elif campo[0][2] == Fore.RED+"\033[1mO\033[0m" and campo[1][1] == Fore.RED+"\033[1mO\033[0m" and campo[2][0] == Fore.RED+"\033[1mO\033[0m":
        campo[0][0] = "'"
        campo[0][1] = "'"
        campo[1][0] = "'"
        campo[1][2] = "'"
        campo[2][1] = "'"
        campo[2][2] = "'"
        carregarJogo(campo)
def verJogador1(campo):
    if campo[0][0] == Fore.BLUE+"\033[1mX\033[0m" and campo[0][1] == Fore.BLUE+"\033[1mX\033[0m" and campo[0][2] == Fore.BLUE+"\033[1mX\033[0m":
        print("Jogador 1 Ganhou")
        exibirResltadoPlayer1(campo)
        return True
    elif campo[1][0] == Fore.BLUE+"\033[1mX\033[0m" and campo[1][1] == Fore.BLUE+"\033[1mX\033[0m" and campo[1][2] == Fore.BLUE+"\033[1mX\033[0m":
        print("Jogador 1 Ganhou")
        exibirResltadoPlayer1(campo)
        return True
    elif campo[2][0] == Fore.BLUE+"\033[1mX\033[0m" and campo[2][1] == Fore.BLUE+"\033[1mX\033[0m" and campo[2][2] == Fore.BLUE+"\033[1mX\033[0m":
        print("Jogador 1 Ganhou")
        exibirResltadoPlayer1(campo)
        return True
    elif campo[0][0] == Fore.BLUE+"\033[1mX\033[0m" and campo[1][0] == Fore.BLUE+"\033[1mX\033[0m" and campo[2][0] == Fore.BLUE+"\033[1mX\033[0m":
        print("Jogador 1 Ganhou")
        exibirResltadoPlayer1(campo)
        return True
    elif campo[0][1] == Fore.BLUE+"\033[1mX\033[0m" and campo[1][1] == Fore.BLUE+"\033[1mX\033[0m" and campo[2][1] == Fore.BLUE+"\033[1mX\033[0m":
        print("Jogador 1 Ganhou")
        exibirResltadoPlayer1(campo)
        return True
    elif campo[0][2] == Fore.BLUE+"\033[1mX\033[0m" and campo[1][2] == Fore.BLUE+"\033[1mX\033[0m" and campo[2][2] == Fore.BLUE+"\033[1mX\033[0m":
        print("Jogador 1 Ganhou")
        exibirResltadoPlayer1(campo)
        return True
    elif campo[0][0] == Fore.BLUE+"\033[1mX\033[0m" and campo[1][1] == Fore.BLUE+"\033[1mX\033[0m" and campo[2][2] == Fore.BLUE+"\033[1mX\033[0m":
        print("Jogador 1 Ganhou")
        exibirResltadoPlayer1(campo)
        return True
    elif campo[0][2] == Fore.BLUE+"\033[1mX\033[0m" and campo[1][1] == Fore.BLUE+"\033[1mX\033[0m" and campo[2][0] == Fore.BLUE+"\033[1mX\033[0m":
        print("Jogador 1 Ganhou")
        exibirResltadoPlayer1(campo)
        return True
def verJogador2(campo):
    if campo[0][0] == Fore.RED+"\033[1mO\033[0m" and campo[0][1] == Fore.RED+"\033[1mO\033[0m" and campo[0][2] == Fore.RED+"\033[1mO\033[0m":
        print("Jogador 2 Ganhou")
        exibirResltadoPlayer2(campo)
        return True
    elif campo[1][0] == Fore.RED+"\033[1mO\033[0m" and campo[1][1] == Fore.RED+"\033[1mO\033[0m" and campo[1][2] == Fore.RED+"\033[1mO\033[0m":
        print("Jogador 2 Ganhou")
        exibirResltadoPlayer2(campo)
        return True
    elif campo[2][0] == Fore.RED+"\033[1mO\033[0m" and campo[2][1] == Fore.RED+"\033[1mO\033[0m" and campo[2][2] == Fore.RED+"\033[1mO\033[0m":
        print("Jogador 2 Ganhou")
        exibirResltadoPlayer2(campo)
        return True
    elif campo[0][0] == Fore.RED+"\033[1mO\033[0m" and campo[1][0] == Fore.RED+"\033[1mO\033[0m" and campo[2][0] == Fore.RED+"\033[1mO\033[0m":
        print("Jogador 2 Ganhou")
        exibirResltadoPlayer2(campo)
        return True
    elif campo[0][1] == Fore.RED+"\033[1mO\033[0m" and campo[1][1] == Fore.RED+"\033[1mO\033[0m" and campo[2][1] == Fore.RED+"\033[1mO\033[0m":
        print("Jogador 2 Ganhou")
        exibirResltadoPlayer2(campo)
        return True
    elif campo[0][2] == Fore.RED+"\033[1mO\033[0m" and campo[1][2] == Fore.RED+"\033[1mO\033[0m" and campo[2][2] == Fore.RED+"\033[1mO\033[0m":
        print("Jogador 2 Ganhou")
        exibirResltadoPlayer2(campo)
        return True
    elif campo[0][0] == Fore.RED+"\033[1mO\033[0m" and campo[1][1] == Fore.RED+"\033[1mO\033[0m" and campo[2][2] == Fore.RED+"\033[1mO\033[0m":
        print("Jogador 2 Ganhou")
        exibirResltadoPlayer2(campo)
        return True
    elif campo[0][2] == Fore.RED+"\033[1mO\033[0m" and campo[1][1] == Fore.RED+"\033[1mO\033[0m" and campo[2][0] == Fore.RED+"\033[1mO\033[0m":
        print("Jogador 2 Ganhou")
        exibirResltadoPlayer2(campo)
        return True

campo = [[1,2,3], [4,5,6], [7,8,9]]

print("----- JOGO da VELHA ------")
print()

carregarJogo(campo)
cont = 0
for x in range(9):
    cont += 1

    jogador1 = input("Jogador 1 [X], Qual posição: ")
    while jogador1 not in ["1","2","3","4","5","6","7","8","9"]:
        print("Valor invalido")
        jogador1 = input("Jogador 1 [X], Qual posição: ")

    while True:
        if jogador1 == "1":
            if campo[0][0] == Fore.BLUE+"\033[1mX\033[0m" or campo[0][0] == Fore.RED+"\033[1mO\033[0m":
                print("Campo ja ocpado, oscolha outro!")
                carregarJogo(campo)
                jogador1 = input("Jogador 1 [X], Qual posição: ")
            else:
                campo[0][0] = Fore.BLUE+"\033[1mX\033[0m"
                carregarJogo(campo)
                break
        elif jogador1 == "2":
            if campo[0][1] == Fore.BLUE+"\033[1mX\033[0m" or campo[0][1] == Fore.RED+"\033[1mO\033[0m":
                print("Campo ja ocupado, escolha outro")
                carregarJogo(campo)
                jogador1 = input("Jogador 1 [X], Qual posição: ")
            else:
                campo[0][1] = Fore.BLUE+"\033[1mX\033[0m"
                carregarJogo(campo)
                break
        elif jogador1 == "3":
            if campo[0][2] == Fore.BLUE+"\033[1mX\033[0m" or campo[0][2] == Fore.RED+"\033[1mO\033[0m":
                print("Campo ja ocupado, escolha outro")
                carregarJogo(campo)
                jogador1 = input("Jogador 1 [X], Qual posição: ")
            else:
                campo[0][2] = Fore.BLUE+"\033[1mX\033[0m"
                carregarJogo(campo)
                break
        elif jogador1 == "4":
            if campo[1][0] == Fore.BLUE+"\033[1mX\033[0m" or campo[1][0] == Fore.RED+"\033[1mO\033[0m":
                print("Campo ja ocupado, escolha outro")
                carregarJogo(campo)
                jogador1 = input("Jogador 1 [X], Qual posição: ")
            else:
                campo[1][0] = Fore.BLUE+"\033[1mX\033[0m"
                carregarJogo(campo)
                break
        elif jogador1 == "5":
            if campo[1][1] == Fore.BLUE+"\033[1mX\033[0m" or campo[1][1] == Fore.RED+"\033[1mO\033[0m":
                print("Campo ja ocupado, escolha outro")
                carregarJogo(campo)
                jogador1 = input("Jogador 1 [X], Qual posição: ")
            else:
                campo[1][1] = Fore.BLUE+"\033[1mX\033[0m"
                carregarJogo(campo)
                break
        elif jogador1 == "6":
            if campo[1][2] == Fore.BLUE+"\033[1mX\033[0m" or campo[1][2] == Fore.RED+"\033[1mO\033[0m":
                print("Campo ja ocupado, escoha outro")
                carregarJogo(campo)
                jogador1 = input("Jogador 1 [X], Qual posição: ")
            else:
                campo[1][2] = Fore.BLUE+"\033[1mX\033[0m"
                carregarJogo(campo)
                break
        elif jogador1 == "7":
            if campo[2][0] == Fore.BLUE+"\033[1mX\033[0m" or campo[2][0] == Fore.RED+"\033[1mO\033[0m":
                print("Campo ja ocupado, escolha outro")
                carregarJogo(campo)
                jogador1 = input("Jogador 1 [X], Qual posição: ")
            else:
                campo[2][0] = Fore.BLUE+"\033[1mX\033[0m"
                carregarJogo(campo)
                break
        elif jogador1 == "8":
            if campo[2][1] == Fore.BLUE+"\033[1mX\033[0m" or campo[2][1] == Fore.RED+"\033[1mO\033[0m":
                print("Campo ja ocupado, escolha outro")
                carregarJogo(campo)
                jogador1 = input("Jogador 1 [X], Qual posição: ")
            else:
                campo[2][1] = Fore.BLUE+"\033[1mX\033[0m"
                carregarJogo(campo)
                break
        elif jogador1 == "9":
            if campo[2][2] == Fore.BLUE+"\033[1mX\033[0m" or campo[2][2] == Fore.RED+"\033[1mO\033[0m":
                print("Campo ja ocupado, escolha outro")
                carregarJogo(campo)
                jogador1 = input("Jogador 1 [X], Qual posição: ")
            else:
                campo[2][2] = Fore.BLUE+"\033[1mX\033[0m"
                carregarJogo(campo)
                break

    if verJogador1(campo):
        break

    if cont == 5:
        print("Empate no game, o jogo deu VELHA!")
        exit()

    jogador2 = input("Jogador 2 [O], Qual posição: ")
    while not jogador2 in ["1","2","3","4","5","6","7","8","9"]:
        print("Valor invalido!")
        jogador2 = input("Jogador 2 [O], Qual posição: ")

    while True:
        if jogador2 == "1":
            if campo[0][0] == Fore.RED+"\033[1mO\033[0m" or campo[0][0] == Fore.BLUE+"\033[1mX\033[0m":
                print("Campo ja ocpado, oscolha outro")
                carregarJogo(campo)
                jogador2 = input("Jogador 2 [O], Qual posição: ")
            else:
                campo[0][0] = Fore.RED+"\033[1mO\033[0m"
                carregarJogo(campo)
                break
        elif jogador2 == "2":
            if campo[0][1] == Fore.RED+"\033[1mO\033[0m" or campo[0][1] == Fore.BLUE+"\033[1mX\033[0m":
                print("Campo ja ocupado, escolha outro")
                carregarJogo(campo)
                jogador2 = input("Jogador 2 [O], Qual posição: ")
            else:
                campo[0][1] = Fore.RED+"\033[1mO\033[0m"
                carregarJogo(campo)
                break
        elif jogador2 == "3":
            if campo[0][2] == Fore.RED+"\033[1mO\033[0m" or campo[0][2] == Fore.BLUE+"\033[1mX\033[0m":
                print("Campo ja ocupado, escolha outro")
                carregarJogo(campo)
                jogador2 = input("Jogador 2 [O], Qual posição: ")
            else:
                campo[0][2] = Fore.RED+"\033[1mO\033[0m"
                carregarJogo(campo)
                break
        elif jogador2 == "4":
            if campo[1][0] == Fore.RED+"\033[1mO\033[0m" or campo[1][0] == Fore.BLUE+"\033[1mX\033[0m":
                print("Campo ja ocupado, escolha outro")
                carregarJogo(campo)
                jogador2 = input("Jogador 2 [O], Qual posição: ")
            else:
                campo[1][0] = Fore.RED+"\033[1mO\033[0m"
                carregarJogo(campo)
                break
        elif jogador2 == "5":
            if campo[1][1] == Fore.RED+"\033[1mO\033[0m" or campo[1][1] == Fore.BLUE+"\033[1mX\033[0m":
                print("Campo ja ocupado, escolha outro")
                carregarJogo(campo)
                jogador2 = input("Jogador 2 [O], Qual posição: ")
            else:
                campo[1][1] = Fore.RED+"\033[1mO\033[0m"
                carregarJogo(campo)
                break
        elif jogador2 == "6":
            if campo[1][2] == Fore.RED+"\033[1mO\033[0m" or campo[1][2] == Fore.BLUE+"\033[1mX\033[0m":
                print("Campo ja ocupado, escoha outro")
                carregarJogo(campo)
                jogador2 = input("Jogador 2 [O], Qual posição: ")
            else:
                campo[1][2] = Fore.RED+"\033[1mO\033[0m"
                carregarJogo(campo)
                break
        elif jogador2 == "7":
            if campo[2][0] == Fore.RED+"\033[1mO\033[0m" or campo[2][0] == Fore.BLUE+"\033[1mX\033[0m":
                print("Campo ja ocupado, escolha outro")
                carregarJogo(campo)
                jogador2 = input("Jogador 2 [O], Qual posição: ")
                break
            else:
                campo[2][0] = Fore.RED+"\033[1mO\033[0m"
                carregarJogo(campo)
                break
        elif jogador2 == "8":
            if campo[2][1] == Fore.RED+"\033[1mO\033[0m" or campo[2][1] == Fore.BLUE+"\033[1mX\033[0m":
                print("Campo ja ocupado, escolha outro")
                carregarJogo(campo)
                jogador2 = input("Jogador 2 [O], Qual posição: ")
            else:
                campo[2][1] = Fore.RED+"\033[1mO\033[0m"
                carregarJogo(campo)
                break
        elif jogador2 == "9":
            if campo[2][2] == Fore.RED+"\033[1mO\033[0m" or campo[2][2] == Fore.BLUE+"\033[1mX\033[0m":
                print("Campo ja ocupado, escolha outro")
                carregarJogo(campo)
                jogador2 = input("Jogador 2 [O], Qual posição: ")
            else:
                campo[2][2] = Fore.RED+"\033[1mO\033[0m"
                carregarJogo(campo)
                break

    if verJogador2(campo):
        break


