#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
#29/09/2023
# HALLAN VICTOR PEREIRA DE ALMEIDA
frase = str(input('Qual frase você quer saber:')).upper().strip()
print('A frase {} contém {} letras A.'.format(frase,frase.count('A')))
print('A primeira vez que a letra A aparece na posição {}'.format(frase.find('A')))
print('A última vez que a letra A aparece na posição {}'.format(frase.rfind('A')))