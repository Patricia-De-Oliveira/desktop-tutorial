from asyncio import sleep
from random import randint
computador = randint(0, 5) #Faz o computador sortia um número entre 0 e 5
print('-=-' * 15)
print('Vou pensar em um número entre 0 e 5. Tente adivinhaar...')
print('-=-' * 15)
jogador = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(2)
if jogador == computador:
    print('Parabéns! Você acertou!')
else:
    print('Você errou! Eu pensei no número {} e não no {}.'.format(computador, jogador))
print('Tente novamente!')