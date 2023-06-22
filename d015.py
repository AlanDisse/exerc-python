#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade dias pelos quais ele foi alugado. Calcule o preço a pagar sabendo que o carro custa RS$60 por dia e R$0,15 por Km rodado.
#22/06/2023
#HALLAN VICTOR PEREIRA DE ALMEIDA
carro = float(input('Quantos km você rodou com o carro?'))
dias = int(input('Por quantos dias você alugou?'))
conta = (dias*60)+(0.15*carro)
print('A conta deu um total de {}'.format(conta))