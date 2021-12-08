# cadeita de testo sempre esta em aspas simplies ou duplas ou uma string
# modos de manipular a cadeia de dados

#tecnica de fatiamento

#ex?

#frase = `Curso em Video`
# Frase [9:13] ele vai pegar a 9 espaço até 0 12 espaço pois o 13 nao entra  e as letras que frase esta recebendo
# é dividigo entre espaços na memoa ex: Curso onde C=0 U=1 R=2 S=3 O=4

#len(frase) qual comprimento da frase?
#frase.cont(('O',0,13) pede pra contas quantas vezes essiste a letra o  do zero ao 13 tem apenas um O
#frase.find('deo') vai indicar onde começa
#frase.find('andoid') se colocar algo dentro do find que nao existe ele retorna -1 significa que nao exite
#'curso' in frase operador in fala existe curso em frase é um operador


#transforção

#frase.replace('Python','andoido)o replace substitu de foorma secundaria de python para android
#frase.upper() (upper é um methodo)  o que for maisculo ele mantem e que for munisculo vai pra maiuscula
#frase.lower ao contratio do upper, vira tudo minusculo
#frase.capitalize ele vai jogar todos os caracteres para minuculo e sómente a 1 letra vira maisculo
#frase.title() ele faz uma analise mais profunda, ele analisa palavra por palavra e deixa a 1 maisculo
# frase ='Aprenda Python'
# frase.strip(frase)
# print(frase)
#Muitas funções tem a variação r ex: rstrip, ele remove somente a direita e da mesma forma tem o lstrip

#Dividir strings
#frase.split() ele dividir em uma lista,
#frase.join(frase) ele vai junta tudo e colocar um espaço
# pratica :
#aspas """  para grandes frases menus etc..
frase = 'Curso em Video Python'
dividido = frase.split()
print(dividido[3])


