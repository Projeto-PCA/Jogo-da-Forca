#Adicionado    .upper() para remover bug na entrada do usuario.
resposta = 'chave'.upper()
acertou = 0
errou = 0
letras_certas = ''
letras_erradas = ''



#Estrutura de repetição para continuar o progama.
while acertou != len(resposta) and errou != 5:
	mensagem = ''
	for letra in resposta:
		if letra in letras_certas:
			mensagem += letra + ' '
		else:
			mensagem += '_ '
	print(mensagem)
	# Entrada Do Usuário.

	letra = input('Insira a letra da Palavra Oculta : ').upper()
	print('Voce ja errou essas letras : ' + letras_erradas)

# Condicional de uma Letra na Resposta

	if letra in resposta:
		print('Voce acertou a Letra: '+ letra)
		letras_certas += letra
		acertou += 1
	else:
		print('Voce errou a Letra: ' + letra)
		letras_erradas += letra
		errou += 1





