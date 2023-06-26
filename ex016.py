#Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a quantidade de cigarros fumados por dias e quantos anos ele já fumou. Considere que um fumante perde 10 min de vida a cada cigarro. Calcule quantos dias de vida um fumante perderá e exiba o total em dias..
#26/06/2023
#HALLAN VICTOR PEREIRA DE ALMEIDA
cigarros_dia= int(input('Quantos cigarros você fumou por dia durante este tempo:'))
anos_fumando= int(input('Quantos anos você fumou durante este tempo:'))
ano_total = anos_fumando*365
vida_perdida = (10*ano_total*cigarros_dia)/1440
print('Você perdeu de vida um total de {}dias'.format(vida_perdida))
