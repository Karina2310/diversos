import random

numero_secreto = random.randint(1, 10)
tentativas = 0

print("🎯 Jogo de Adivinhação (1 a 10)")

while True:
    tentativa = int(input("Digite seu palpite: "))
    tentativas += 1

    if tentativa == numero_secreto:
        print(f"Parabéns! Você acertou em {tentativas} tentativas.")
        break
    elif tentativa < numero_secreto:
        print("Tente um número maior.")
    else:
        print("Tente um número menor.")
