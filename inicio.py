import random
from random import choice

#Arquivo para puxar as palavras secretas para as respostas.
with open('palavras.txt') as arquivo:
    linhas = arquivo.read()

x = range(8)
n = random.choice(x)
lista_de_respostas = linhas.split('\n')
listaIndice = lista_de_respostas[n].split(':')
resposta = listaIndice[0].upper()
dica = listaIndice[1]

if dica == 'vidro':
    msgdica = f'Jogar na lixeira verde referente a {dica}'
if dica == 'plastico':
    msgdica = f'Jogar na lixeira vermalha referente a {dica}'
if dica == 'metal':
    msgdica = f'Jogar na lixeira amarelo referente a {dica}'
if dica == 'não reciclaveis':
    msgdica = f'Jogar na lixeira preto referente a Não'
if dica == 'papel':
    msgdica = f'Jogar na azul verde referente a {dica}'
if dica == 'organico':
    msgdica = f'Jogar na lixeira marrom de referente a {dica}'
acertou = 0
errou = 0
letras_certas = ''
letras_erradas = ''

# Saidas padronizadas de chances do boneco.
nada = ''
forca = """	
	____
	    |
	    |
	    |
	    -"""
cabeca = """
	    O
	"""
tronco = """
	    O
	    |
	"""
braco_esquerdo = """
	    O
	    |
	"""

braco_direito = """
	    O
	   /|\\
	"""
perna_esquerda = """
	    O
	   /|\\
	   / 
	"""
perna_direita = """
	    O
	   /|\\
	   / \\
	"""
chances_do_boneco = [nada, cabeca, tronco, braco_esquerdo, braco_direito, perna_esquerda, perna_direita]

# Estrutura de repetição para continuar o progama.
while acertou != len(resposta) and errou != 7:
    # Parte do progama responsavel pela saida da Palavra Secreta
    mensagem = ''
    for letra in resposta:
        if letra in letras_certas:
            mensagem += f'{letra}'
        else:
            mensagem += '_ '
    print('<---Dica da Palavra Secreta--->')
    print(msgdica)
    print(forca + chances_do_boneco[errou])
    print(mensagem)
    # Entrada Do Usuário.

    letra = input('Insira a letra da Palavra Oculta : ').upper()
    # saida

    # Condicional de uma Letra na Resposta
    if letra in letras_certas + letras_erradas:
        print('Você ja tentou esta letra antes!!')
        continue
    if letra in resposta:
        print('Voce acertou a Letra: ' + letra)
        letras_certas += letra
        acertou += resposta.count(letra)
    else:
        print('Voce errou a Letra: ' + letra)
        letras_erradas += letra
        errou += 1

