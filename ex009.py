#Faça um algoritmo que leia quanto dinheiro uma pessoa tem na carteira (em R$) e mostre quantos dólares ela pode comprar. Considere US$1,00 = R$4,77.
#21/06/2023
#HALLAN VICTOR PEREIRA DE ALMEIDA
dinheiro_carteira = float(input('Quanto você tem na carteira?'))
dolar_dinheiro = dinheiro_carteira/4.77
print('Você pode comprar',str(dolar_dinheiro)+'$','USD')