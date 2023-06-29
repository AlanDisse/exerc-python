# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".
#29/09/2023
# HALLAN VICTOR PEREIRA DE ALMEIDA
cidade = input('Em que cidade você nasceu?').strip()
print('A frase começa com santo?:{}'.format('SANTO' in cidade[:5].upper() =='SANTO'))