#O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos launos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
#22/06/2023
#HALLAN VICTOR PEREIRA DE ALMEIDA
from random import shuffle
primeiro_aluno = input('Primeiro aluno:')
segundo_aluno = input('Segundo aluno:')
terceiro_aluno = input('Terceiro aluno:')
quarto_aluno = input('Quarto aluno:')
lista_escolhido = [primeiro_aluno,segundo_aluno,terceiro_aluno,quarto_aluno]
shuffle(lista_escolhido)
print('O aluno escolhido foi {}.'.format(lista_escolhido))