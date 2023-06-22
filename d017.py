#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
#22/06/2023
#HALLAN VICTOR PEREIRA DE ALMEIDA
cateto_adjacente = float(input('Digite o valor do cateto adjacente:'))
cateto_oposto = float(input('Digite o valor do cateto oposto'))
hipotenusa = cateto_adjacente**2 + cateto_oposto**2
print('O valor da hipotenusa é {} * {}'.format(hipotenusa,hipotenusa))