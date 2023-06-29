#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
#29/06/2023
# HALLAN VICTOR PEREIRA DE ALMEIDA
nome_completo = str(input('Digite o nome completo:')).strip()
n = nome_completo.split()
print('O primeiro nome é: {}'.format(n[0]))
print('O último nome é {}'.format(n[len(n)-1]))