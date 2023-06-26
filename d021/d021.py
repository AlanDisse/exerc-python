#Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3
#26/06/2023
#HALLAN VICTOR PEREIRA DE ALMEIDA
import pygame
pygame.init()
pygame.mixer.music.load('d021.mp3')
pygame.mixer.music.play()
pygame.time.delay(1000)
pygame.event.wait()