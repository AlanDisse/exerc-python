# Crie um programa que leia um número Real qualuqer pelo teclado e mostre na tela a sua porção inteira.
#22/06/2023
#HALLAN VICTOR PEREIRA DE ALMEIDA
import math
numero_int = float(input('Digite um número:'))
print('O número {} tem a parte inteira {}'.format(numero_int,math.floor(numero_int)))