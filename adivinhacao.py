print("*******************")
print("Bem vindos ao jogo de adivinhação!")
print("*******************")

numero_secreto = 42
total_de_tentativas = 3
rodada = 1

while (rodada <= total_de_tentativas > 0):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chute = input("Digite o seu número: ")
    print("Você digitou ", chute)
    chute = int(chute)

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou):
        print("Você acertou!")
    else:
        if(maior):
            print("Errado. Seu chute foi maior do que o número secreto!")
        elif(menor):
            print("Errado. Seu chute foi menor do que o número secreto!")

    rodada = rodada + 1



print("Fim de jogo!")


