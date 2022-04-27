import random

print('JOGO DE ADIVINHAÇÃO')

numero_escolhido = int(input('Digite um número entre 0 e 20: '))

numero_secreto = random.randint(0 , 21)

if numero_escolhido == numero_secreto:
    print(f'O número era {numero_secreto} você acertou')

else:
    print(f'O número correto era {numero_secreto} você errou!')
