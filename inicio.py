#Adicionado    .upper() para remover bug na entrada do usuario.
resposta = 'chave'.upper()
acertou = 0
errou = 0
letras_certas = ''
letras_erradas = ''

#Estrutura de repetição para continuar o progama.
while acertou != len(resposta) and errou != 5:
	# Entrada Do Usuário.

	letra = input('Insira a letra da Palavra Oculta : ').upper()
	print('Voce ja acertou essas letras : ' + letras_certas)
	print('Voce ja errou essas letras : ' + letras_erradas)

# Condicional de uma Letra na variavel Resposta.

	if letra in resposta:
		print('Você acertou a Letra!!')
		letras_certas += letra
		acertou += 1
	else:
		print('Você errou a Letra!!')
		letras_erradas += letra
		errou += 1





