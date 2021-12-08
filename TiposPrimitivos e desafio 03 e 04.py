#Tipos primitivos de variaveis

# n1=int (input('Digite um numero :'))
# n2=int (input('Digite um numero :'))
# s= n1+n2
# print('A soma vale',s)

#Exemplo de int() tudo que estiver dentro de um parenteses é um int
# int , float , bool , srt
#Ex: 
# int (4 , 5, 5,-9)
# float (4.5, 0.76, -15.223, 7.0) tem parte flutuante
# bool True  ou False
# srt(string) 'olá' palavras '7.5' ''

# print('A soma Vale :{}'.format(s)) usando sintaxe .format

#forma diferente de printar na tela

# n1 =int (input('Digite um valor: '))
# n2 =int (input('Digite um valor: '))
# s= n1+n2
# # print('A soma entre {} e {}'.format(n1 ,n2), 'Vale',s) meu jeito, do jetio dele usuou 3 mascaras{}
# print('Soma entre {} e {} é {}'.format(n1, n2, s))
#Metodo 
# 'isnumeric' verifica se é possivel transformar para numero
# 'isalpha' verifica se é letra 
#  'isalnum' Verifica se é alphanumerico
#  'isupper' Verifica se esta somente com maisculas


# n=input('Digite um valor:')
# print(n.isalnum())



# Desafios 003 Feito

# n1 =int(input('Digite um  numero'))
# n2 =int(input('Digite um numero'))
# t= n1+n2
# print('valor entre {} e {} é {}'.format(n1 ,n2 , t))

# Desafios 004 feito porém nao mostrou todas as informações

# n=input('Digite alguma coisa:')
# print(type(n),n.isalpha())

# metodo do guanabara
a =input('digite algo: ')
print('o Tipo primitivo é : ',type (a))
print('Só tem espaços ?',a.isspace())
print('é um numero ?',a.isnumeric())
print('é alfabetico ?',a.isalpha())
print('é alphanumerico ?',a.isalnum())
print('esta em maiusculas? ',a.isupper())
print('esta em minusculas ? ',a.islower())
print('esta em capitalizado ? ',a.istitle())