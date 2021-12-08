import math
import random
import pygame
# crie um programa que leia um numero real qualquer "pelo teclado"
# d15 = float(input('Insira um numero qualquer com virgula : '))
# inte = math.trunc(d15)
# # e mostr na tela a sua porção inteira
# print('O valor inteiro de {} é {} '.format(d15, inte))


# d17 faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo,

# d1 = float(input('Digite o valor do cateto oposto : '))
# d2 = float(input('Digite o valor do cateto adjacente'))
# res = math.hypot(d1, d2)
# # calcule e mostro o comprimento da hipotenusa
# print("o resultado da hipotenusa é {:.2f}".format(res))

# Exercício Python 18: Faça um programa que leia um ângulo qualquer
# d18 = float(input('Digite um angulo qualquer :'))
# dr = math.radians(d18)
# # e mostre na tela o valor do seno, cosseno e tangente desse ângul
# cos = math.cos(dr)
# sen = math.sin(dr)
# tan = math.tan(dr)
# print('O seno desse angulo é {:.2f},\nO cosseno é {:.2f}\nE a tangende desse angulo é {:.2f}'.format(sen,cos,tan))

# Exercício Python 19: Um professor quer sortear um dos seus quatro alunos para apagar o quadro
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

# d19 = str(input('Digite o nome de um aluno :'))
# d19 = str(input('Digite o nome de um Aluno : '))
# d191 = str(input('Digite o nome de um Aluno : '))
# d192 = str(input('Digite o nome de um Aluno : '))
# d193 = str(input('Digite o nome de um Aluno : '))
# d194 = str(input('Digite o nome de um Aluno : '))
#
# lista_nomes = [d191, d191, d192, d193, d194]

# sorteio = random.choice(lista_nomes)
#
# print('O aluno sorteado foi :', sorteio)

#Exercício Python 20: O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos
# . Faça um programa que leia o nome dos quatro alunos
# n1 = input("digite o nome do aluno")
# n2 = input("digite o nome do aluno")
# n3 = input("digite o nome do aluno")
# n4 = input("digite o nome do aluno")
# lista_nomes = [n1, n2, n3, n4]
# random.shuffle(lista_nomes)
# # e mostre a ordem sorteada.
# print('A ordem de apresentação sera {}:'.format(lista_nomes))

#Exercício Python 21: Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
# pygame.mixer.init()
# pygame.init()
# pygame.mixer.music.load('imd.mp3')
# pygame.mixer.music.play(loops=0,start=0.0)
# pygame.event.wait()


# d22Crie um programa que leia o nome de uma pessoa

# d22 =input('Digite seu nome ').strip()
# print('Seu nome minusculo é {}'.format(d22.lower()))
# print('seu nome Maisculo é {}'.format(d22.upper()))
# print('Seu nome tem {} Letras'.format(len(d22) - d22.count(' ')))
# print('Seu 1 nome tem {} Letras'.format(len(d22[0:6])))
# e mostre o nome com todas maisculas, minusculas ,quantas letras sem considerar espaços e Quantas letras tem 1 nome

#Exercício Python 23: Faça um programa que leia um número de 0 a 9999
d23 = int(input('Digite um numero : '))
un =str(d23)
print('Analisando o Numero que voce digitou {}'.format(d23))
print('Unidade {}'.format(un[3]))
print('Dezena {}'.format(un[2]))
print('Centena 0')
print('Milhar 0')
print('Centena {}'.format(un[1]))
print('Milhar {}'.format(un[0]))


# mostre na tela cada um dos dígitos separados.