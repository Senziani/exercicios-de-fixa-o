from datetime import date

# Apenas para Curso em VIdeo e também o arquivo Aula03

# Meta 100 exercicios

# Desafio001
# Crie um programa olá mundo

# print('Olá, Mundo!')
# ou como varialvel

# v1 = 'Olá, Mundo!'
# print(v1)

# -----------------------------------------------------
# Desafio 002
# Scrpit que leia nome e de boas vindas
# nome= input ('Qual é seu nome?')

# print('Olá '+ nome +' Prazer em te conhecer')
# Exemplo de saida formatada

# nome= input ('Qual é seu nome?')

# print('Olá {}!'.format(nome) ,' Prazer em te conhecer')


# -----------------------------------------------------
# Exercicios 03   Somando valores    Feito e correto
# n1 = int(input('Digite um valor: '))
# n2 =int(input('Digite um valor: '))

# soma= n1+n2
# print('A soma de {} e {} é igual a {}'.format(n1, n2, soma))


# Desafio 005 Faça um programa que leia um numero inteiro e mostre
# antecessor e sucessor Feito

# d5=int(input('Digite um numero')) 
# print('O antecessor deste valor é {} \n E o seu sucessor é {:>}'.format((d5-1),d5+1))

# Desafio 06
# Crie um algoritimo que leia um numero e mostre o seu dobro, triplo e raiz quadrada

# d6=int(input('Digite um valor'))
# print('O dobro desse valor é {}\n O triplo é {}\n E a raiz é {}'.format((d6*2),(d6*3),(d6*(1/2))))

# D7- Desenvolva um programa que leia as duas notas e de um aluno e calcule a media

# n1 = int(input('Qual a nota P1'))
# n2 = int(input('Digite a nota da P2'))
# nota_final = (n1 + n2) / 2
# if nota_final >= 7:
#     print(f'A nota dele é {nota_final}, portanto ele foi aprovado')
# if nota_final <= 7:
#     print(f'A nota Final dele é {nota_final}, infelizmente ele foi repravado')


# D8 -  escreva um programa leioa um valor em metros  e o exiba convertido centrimetros  e milimetros

# m = float(input('entre com o valor para ser convertido')) #ins somente em casos de numero interos
#
# c  = m*100
# mi = m*10000   #errado era mil
# hm = m*10
# dam = m*100
#
#
# print(f'o valor em Centrimetros é {c} cm \n Em milimetros é {mi} mm')


# Digite um valor  e ele mostre sua tabuada

# tabuada = ['1','2','3','4','5','6','7','8','9','10']
#
# tab = int(input('Digite um numero:'))

# while tab in tabuada < 0 :
#     print(f'{tab}')
# metodo do guanabara
# print('---'*12)
# print(' {} x {:2} = {}'.format(tab,1,tab*1))
# print(' {} x {:2} = {}'.format(tab,2,tab*2))
# print(' {} x {:2} = {}'.format(tab,3,tab*3))
# print(' {} x {:2} = {}'.format(tab,4,tab*4))
# print(' {} x {:2} = {}'.format(tab,5,tab*5))
# print(' {} x {:2} = {}'.format(tab,6,tab*6))
# print(' {} x {:2} = {}'.format(tab,7,tab*7))
# print(' {} x {:2} = {}'.format(tab,8,tab*8))
# print(' {} x {:2} = {}'.format(tab,9,tab*9))
# print(' {} x {:2} = {}'.format(tab,10,tab*10))
# print('---'*12)

# converter dinheiro

# dol = float(input("Quando Dinheiro voce te ma carteira? R$"))
# conv = dol / 5.57
# hoje = date.today()
# coneu = dol / 6.24
# print('Segundo a conversão do dia {} , com R${:.2f} reais\n você pode comprar U$${:.2f} Dollares\n ou até {} Euros'.format(hoje, dol, conv,coneu))


# Faça um programa  que leia a largura e a altura de uma parede em metros ,calcule a sua área
# e aquanditidade de tinta necessaria para pintala , sabendo que cada litro de titinta pinta uma parede de
# 2m^2
#desafio 011
# largura = float(input('Entre com a Largura da parede: '))
# altura = float(input('Entre com a altura da parede : '))
# tinta = 2 ** (1 / 2)
# # area = b.h formula
# area = largura * altura
# pintada = area/2

# print('A sua parede tem a dimenção de {} x {} e a  área da parede é {}m 2'.format(largura,altura,area))
# print ('para pintar essa parede voce prescisa de {:.2f}l de tintas'.format(pintada))


# Desafio 12
# Meu metodo
# d12 = float(input('Qual o preço do produto? R$'))
# desc = 0.05
# # desapli =d12* desc
# # tot = d12-desapli
# preco = d12 - (d12 * 5 / 100) #guanabara
# print('O preço do produto era R${} e com {}% de desconto\n passou a custar R${:.2f}'.format(d12,desc,preco))

#Desafio 13
# Exercício Python 13: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

# sal= float(input('Qual o salario atual do funcionario ? R$'))
# aum='15'
# novosal = sal +(sal * 15 / 100)
# print('O Salario do funcionario era {} e  com o aumento de {}% passou a ser  R${:.2f}'.format(sal,aum,novosal))

#Exercício Python 14: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
# c = float(input('Informe a temperatura em C :'))
# f =((9 * c)/5)+32
# print('A temperatura de {}C corresponde a {} F!'. format(c,f))

## Exercício Python 15: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

#quantidades de Km percorrido por um carro alugado
km = float(input('Quantos Km o veiculo rodou?'))
#Quantidade de dias alugado
dia = int(input('Quantos dias o veiculo foi alugado?'))
#Calcular quando vai pagar sabendo que  o o carro custa 60 por dia e  0,15 por km rodado
caldia = (dia * 60)
kmrod = (km * 0.15 )
pag = caldia + kmrod
print('De acordo com os dados o carro andou {}KM,foi alugado por {} dias\n o valor a ser pago e R${:.2f}'.format(km,dia,pag))



