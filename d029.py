#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
#30/06/2023
#HALLAN VICTOR PEREIRA DE ALMEIDA
velocidade_carro = int(input('Digite a velocidade do carro:'))
multa = (velocidade_carro - 80)*7
if velocidade_carro > 80:
    print('Você foi multado em {}$'.format(multa))
else:
    print('Você não foi multado')