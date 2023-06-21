#Faça um algoritmo que leia a largura e altura de uma parede, calcule e mostre a área a ser pintada e a quantidade de tinta necessária para o serviço, sabendo que cada litro de tinta pinta uma área de 2metros quadrados.
#21/06/2023
#HALLAN VICTOR PEREIRA DE ALMEIDA
altura = int(input('Qual é a altura da parede (em m)?'))
largura = int(input('Qual é a largura da parede (em m)?'))
area = altura*largura
tinta_area = area/2
print('A área a ser pintada é de {}m, e a quantidade de tinta que você vai precisar é de {}L'.format(area,tinta_area))