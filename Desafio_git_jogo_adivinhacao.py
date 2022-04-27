import random

print('JOGO DE ADIVINHAÇÃO')

tentativas = 5

numero_secreto = random.randint(0 , 21)

while tentativas > 0:
    
    numero_escolhido = int(input('Digite um número entre 0 e 20: '))

    if numero_escolhido == numero_secreto:
        print(f'O número era {numero_secreto} você acertou!')
        break

    elif numero_escolhido < numero_secreto:
        print('Você errou, o número secreto é maior que o seu palpite!')
        
    elif numero_escolhido > numero_secreto:
        print('Você errou, o número secreto é menor que o seu palpite!')
        
    tentativas -= 1
    print(f'Você tem {tentativas} tentativas.')
print('FIM DO JOGO!')
