#coding: utf-8
from gui import * 
from func import *

dic_perguntasRespostas = recuperaPerguntasRespostas()
listaPerguntas = []

for x in dic_perguntasRespostas:
	listaPerguntas.append(x)
	#print(">>",x)

pergunta = escolhePergunta(dic_perguntasRespostas)
#dic_perguntasRespostas.pop(pergunta)



iniciaInterface()


