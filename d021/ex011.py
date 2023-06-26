#Desenvolva uma lógica que leia os valores de A, B e C de uma equação do segundo grau e mostre o valor de Delta.
#26/06/2023
#HALLAN VICTOR PEREIRA DE ALMEIDA
A = int(input('Digite o primeiro valor:'))
B = int(input('Digite o segundo valor:'))
C = int(input('Digite o terceiro valor:'))
delta = B**2-4*A*C
print('O valor de  delta é {}'.format(delta))