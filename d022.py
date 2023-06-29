#Exercício Python 022: Crie um programa que leia o nome completo de uma pessoa e mostre: 
#- O nome com todas as letras maiúsculas e minúsculas.
#- Quantas letras ao todo (sem considerar espaços).
#- Quantas letras tem o primeiro nome.
# 29/06/2023
#HALLAN VICTOR PEREIRA DE ALMEIDA
nome_completo = input('Digite seu nome completo:')
print('O nome completo em letra maíuscula é: {}'.format(nome_completo.upper()))
print('O nome completo em letra minúscula é: {}'.format(nome_completo.lower()))
print(len(nome_completo.strip()))
print('Seu primeiro nome tem {} letras'.format(nome_completo.find(' ')))

