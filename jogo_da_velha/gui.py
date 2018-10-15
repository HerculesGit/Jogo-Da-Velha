#coding: utf-8
# importacao de biblioteca
from tkinter import Tk, Label, PhotoImage, Button
from tkinter.messagebox import showinfo
from func import *
import sys
import os

# 1 - executando
# 2 - continuou

def restart_program():
	naoContinuar()
	python = sys.executable
	os.execl(python, python, * sys.argv)

def continuar_program():
	setStatus("2")
	#print("status",recuperaStatus())
	escreveContinuar(dic_perguntasRespostas)
	python = sys.executable
	os.execl(python, python, * sys.argv)

if (recuperaStatus() == "1"):
	naoContinuar()
#print("status",recuperaStatus())


dic_perguntasRespostas = recuperaPerguntasRespostas()
pergunta, resposta = escolhePergunta(dic_perguntasRespostas)
dic_perguntasRespostas.pop(pergunta)
#print(len(dic_perguntasRespostas))

#print("Pergunta selecionada: ", pergunta, resposta)

respostaJogador = []
for i in range(100):
	respostaJogador.append("")

indicePilha = 6	# 0 a 6
qtdErro = 0

listaLabels = []
listaLabelsResposta = [] 		# quantidade de labels que é usado para a resposta
listaImagens = []
listaBotoes = []
listaTeclasPressionadas = []	# coloca todas as posicoes das teclas pressionadas
listaTeclasClicadas = []
l_teclado= []


raiz = Tk()
raiz.title('Jogo da Forca')		# configuracoes do titulo tela/window
raiz.geometry("800x535")		# configuracao do tamanho da tela raiz.resizable(0,0)


foto = PhotoImage(file="image/fundo1.png") #
background = Label(master=raiz, image=foto, width=800, height=535)
background.place(x=0,y=0)
labelPergunta = Label(master=raiz, text=pergunta).place(x=15,y=17)
pontuacaoErros = Label(master=raiz, text=str(qtdErro)).place(x=595,y=110)

btRestart = Button(master=raiz, text= "Reiniciar", command=restart_program)
btRestart.config(state='disable')
#btRestart.config(bg='green')
btRestart.place(x=15,y=500)

btContinuar = Button(master=raiz, text= "Continuar", command=continuar_program)
btContinuar.place(x=690,y=500)
btContinuar.config(state='disable')

def desempilhar():
	global indicePilha
	if (indicePilha > 0):
		listaLabels[indicePilha].place(x=2400,y=120)
		indicePilha -=1
		#print(indicePilha)

# Posiciona os labels
def empilhar():
	for label in listaLabels:
		label.place(x=40,y=50)

def criaLabesRespostas():
	global resposta
	x = 90
	y = 330
	for i in range(len(resposta)-1):
		label = Label(master=raiz, text="_")
		label.config(font=("Courier", 20))
		listaLabelsResposta.append(label)
		listaLabelsResposta[i].place(x=x,y=y)
		x+=20

def criaLabels():
	global pergunta
	for img in listaImagens:
		listaLabels.append(Label(master=raiz, image=img, width=520, height=270))
	Label(master=raiz, text="Erros").place(x=582,y=77)

def carregaImagens():
	for i in range(7):
		caminho = "image/{0}.png".format(i)
		#print(caminho)
		listaImagens.append(PhotoImage(file=caminho))

#def pegaTexto(b):
	#print("chupe")
	#print(b.cget('text'))


def desabilitaTeclado():
	global l_teclado
	for i in range(len(l_teclado)):
		l_teclado[i].config(state='disable')

def verificaTeclaPressionada(botao):		# verifica a tela clicada
	global qtdErro
	global pontuacaoErros
	#print(botao.cget('text'))

	# se a letra nao estiver na palavra
	if (validaLetra(botao.cget('text'), resposta) == False):
		#print("Errou")
		botao.config(bg='red')
		desempilhar()
		qtdErro+=1
		pontuacaoErros = Label(master=raiz, text=str(qtdErro)).place(x=595,y=110)

		# perde?
		if (isLose(qtdErro)):
			desabilitaTeclado()
			btRestart.config(state='normal')
			showinfo(message=":'( Você consegue fazer melhor!\n\nClique em 'Reiniciar' e tente novamente")


	else:	# se estiver
		botao.config(bg='green')
		mudaLabel(botao.cget('text'))
		#print("<>",isWinner(respostaJogador, resposta)) 	# resposta Jogador eh uma lista, resposta eh uma string

		# se ganhou
		if (isWinner(respostaJogador, resposta)):
			btContinuar.config(state='normal')
			desabilitaTeclado()
			if(len(dic_perguntasRespostas) == 0):
				showinfo(message=r"\0/Parabéns, você conseguiu zerar! Mostrou quem é bom/boa! Clique em continuar ou feche a janela")

			else:
				showinfo(message="Parabéns, você conseguiu acertar!\n\nClique em 'Continuar' e mostre quem é que manda")

		#print(isWinner())
	botao.config(state='disable')

def mudaLabel(letra):
	indice = 0
	for i in resposta:
		#print("{0}, {1}".format(letra, resposta))
		if (letra == i):
			listaLabelsResposta[indice].config(text=letra)
			respostaJogador[indice] = letra
		indice+=1
	#print(">>",respostaJogador)



def criaTeclado():		# criacao do teclado | 26 teclas
	global l_teclado 
	listaLetrasTecladoQwerty = ['Q','W','E','R','T','Y','U','I','O','P',
		'A','S','D','F','G','H','J','K','L',
		'Z','X','C','V','B','N','M']

	l = 0
	x = 98
	y = 346 + 30# mais 40 pixels
	for i in range(26):
		bt = Button(raiz, text=listaLetrasTecladoQwerty[l]) #command=desempilhar) #height=0, width=0)
		
		if (i < 9):				# primeira linha  0 - 9
			bt.place(x=x, y=y)

		elif (i < 19):				# segunda linha 10 - 19
			bt.place(x=x, y=y)

		elif (i >=18 ):				# terceira linha 10 - 19
			bt.place(x=x, y=y)
		
		bt.configure(command=lambda b=bt: verificaTeclaPressionada(b))

		x+=41
		l+=1
		# configura x e y
		if (i == 9):		# linha 2
			x=119
			y=384 + 30
		elif (i == 18):		# linha 3
			x=160
			y=422 + 30

		l_teclado.append(bt)


carregaImagens()		# carregamento das imagens para a memoria
criaLabels()			# carregamento de labels para a memoria
criaLabesRespostas()	# label da resposta
empilhar()				# posicionamento de labels 
criaTeclado()			# carrega teclado e posiciona-o


def iniciaInterface():
	pass

setStatus("1")
raiz.mainloop()

# executar a tela raiz
#raiz.mainloop()