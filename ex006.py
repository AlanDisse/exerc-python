#Faça um programa que leia um número inteiro e mostre o seu antecessor e seu sucessor.
#20/06/2023
#HALLAN VICTOR PEREIRA DE ALMEIDA
numero = int(input('Digite um número:'))
antecessor = numero - 1
sucessor = numero +1
print('{}é o antecessor de {} e {}é o sucessor.'.format(antecessor,numero,sucessor))