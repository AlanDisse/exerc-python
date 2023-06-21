# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento
#20/06/2023
#HALLAN VICTOR PEREIRA DE ALMEIDA
salario = float(input('Qual é seu salário?'))
salario_aument = salario+(salario*15/100)
print('Seu salário atual é de {}$, e agora vai ser de {}$'.format(salario,salario_aument))
