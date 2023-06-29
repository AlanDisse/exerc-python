#Exercício Python 023: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
#29/06/2023
#HALLAN VICTOR PEREIRA DE ALMEIDA
numero_info = int(input('Digite um número sem ter casas decimais entre 1 e 9999:'))
u = numero_info // 1 % 10
d= numero_info // 10 % 10
c = numero_info//100 % 10
m = numero_info//1000 % 10
print('Analisando o número {}'.format(numero_info))
print('A unidade é: {}'.format(u))
print('A dezena é: {}'.format(d))
print('A centena é: {}'.format(c))
print('O milhar é: {}'.format(m))