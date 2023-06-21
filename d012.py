# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
#21/06/2023
#HALLAN VICTOR PEREIRA DE ALMEIDA
preco_desc = float(input('Qual o valor do produto?'))
precocom_desc = preco_desc - (preco_desc*5/100)
print('O valor do produto com desconto fica {}$'.format(precocom_desc))