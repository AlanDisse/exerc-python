#Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
# 29/09/2023
# HALLAN  VICTOR PEREIRA DE ALMEIDA
nome = str(input('Digite pra verificar se você tem "SILVA NO NOME"'))
print('O resultado é: {}'.format('SILVA' in nome.upper().split()))