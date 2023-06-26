#Um professor quer sortear um dos seus quatro alunos par aapagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
#26/06/2023
#HALLAN VICTOR PEREIRA DE ALMEIDA
import random
primeiro_aluno = input('Primeiro aluno:')
segundo_aluno = input('Segundo aluno:')
terceiro_aluno = input('Terceiro aluno:')
quarto_aluno = input('Quarto aluno:')
lista_escolhido = [primeiro_aluno,segundo_aluno,terceiro_aluno,quarto_aluno]
aluno_escolhido = random.choice(lista_escolhido)
print('O aluno escolhido foi {}.'.format(aluno_escolhido))