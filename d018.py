#Faça um programa que leia um Ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo
#22/06/2023
#HALLAN VICTOR PEREIRA DE ALMEIDA
import math

angulo = float(input('Digite o valor do ângulo em graus: '))
angulo_radianos = math.radians(angulo)

seno = math.sin(angulo_radianos)
cosseno = math.cos(angulo_radianos)
tangente = math.tan(angulo_radianos)

print('Seno: {:.2f}'.format(seno))
print('Cosseno: {:.2f}'.format(cosseno))
print('Tangente: {:.2f}'.format(tangente))




