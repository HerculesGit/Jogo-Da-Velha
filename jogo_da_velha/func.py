#!/usr/bin/env python
#coding: utf-8
from random import randint


# 0 - fechou com o x
# 1 - reiniciou
# 2 - continuou
def recuperaStatus():
	arq = open('data/seguranca.txt', 'r',encoding="latin-1")
	texto = arq.readline()#.decode('utf-8')
	return texto

def setStatus(status):
	arq = open('data/seguranca.txt', 'w',encoding="latin-1")
	arq.write(status)

	arq.close()

#print(recuperaStatus())
#setStatus("2")

def recuperaPerguntasRespostas():
	
	arq = open('data/continuar.txt', 'r',encoding="latin-1")
	texto = arq.readlines()#.decode('utf-8')
	if (len(texto) == 0):
		#print("entou")
		arq = open('data/perguntas_respostas.txt', 'r',encoding="latin-1")
		texto = arq.readlines() #.decode('utf-8')

	#print(texto)
	# pergunta : resposta
	perguntas_respostas = {}
	for linha in texto:

		#print(linha)

		if (len(linha)>=2):		# garante que se ela deu um ENTER no final nao deh erro
			#if(len(linha))
			chave, valor = linha.split(';')
			perguntas_respostas[chave] = str(valor)
			#print(linha)
		#print(len(linha))
		
	#print(perguntas_respostas)
	arq.close()
	return perguntas_respostas

def escreveContinuar(dicionario):
	arq = open('data/continuar.txt', 'w',encoding="latin-1")
	for pergunta in dicionario:

		arq.write("{0};{1}".format(pergunta, dicionario.get(pergunta)))

	arq.close()

def naoContinuar():
	arq = open('data/continuar.txt', 'w',encoding="latin-1")
	arq.write("")
	arq.close()

# resposta Jogador eh uma lista, resposta eh uma string
def isWinner(respostaJogador, resposta):
	for indice in range(len(resposta)-1):
		#print("comparando {0}-{1}".format(respostaJogador[indice],resposta[indice]))
		
		if(respostaJogador[indice] == resposta[indice]):
			pass #print("if {0}-{1}".format(respostaJogador[indice],resposta[indice]))
		else:
			#print("else {0}-{1}".format(respostaJogador[indice],resposta[indice]))
			return False

	return True

def isLose(qtdErro):
	return qtdErro == 6


def escolhePergunta(dicionario):
	print("size",len(dicionario))
	lista_perguntas = []
	if (len(dicionario)>0):
	
		for p in dicionario:
			lista_perguntas.append(p)
			#lista_perguntas.append(str(dicionario.get(p)))

		escolha = lista_perguntas[randint(0,len(dicionario)-1)]

		# pergunta, resposta
		return escolha, str(dicionario.get(escolha))

	for l in dicionario:
		lista_perguntas.append(l)
	return lista_perguntas[0], str(dicionario.get(lista_perguntas[0]))

def validaLetra(letra, resposta):
	'a letra que eh passada como argumento e verifica se ta na palavra'

	return str.upper(letra) in resposta

#dicionario = recuperaPerguntasRespostas()
#print(dicionario.get("Qual célula não apresenta membrana plasmáica?"))
#print(validaLetra('j',"Qual célula não apresenta membrana plasmáica?"))

#print(escolhePergunta(recuperaPerguntasRespostas()))