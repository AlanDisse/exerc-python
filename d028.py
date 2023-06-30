#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
#30/06/2023
#HALLAN VICTOR PEREIRA DE ALMEIDA
from random import randint
numero_aleatorio = randint(0,5)
numero_escolhido = int(input('Digite um número entre 1 e 5 e veja se acertou:'))
if numero_aleatorio == numero_escolhido:
    print('Você ganhou!')
else:
    print('Você perdeu.')
