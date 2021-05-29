#Adicionado    .upper() para remover bug na entrada do usuario.
resposta = 'chave'.upper()
acertou = 0
errou = 0
letras_certas = ''
letras_erradas = ''


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
#Estrutura de repetição para continuar o progama.
while acertou != len(resposta) and errou != 7:
	#Parte do progama responsavel pela saida da Palavra Secreta
	mensagem = ''
	for letra in resposta:
		if letra in letras_certas:
			mensagem += f'{letra}'
		else:
			mensagem += '_ '

	print(forca + chances_do_boneco[errou])
	print(mensagem)
	# Entrada Do Usuário.

	letra = input('Insira a letra da Palavra Oculta : ').upper()
	# saida
	

# Condicional de uma Letra na Resposta

	if letra in resposta:
		print('Voce acertou a Letra: '+ letra)
		letras_certas += letra
		acertou += 1
	else:
		print('Voce errou a Letra: ' + letra)
		letras_erradas += letra
		errou += 1





