#Adicionado .	upper para remover bug na entrada do usuario
resposta = 'chave'.upper()
# Entrada Do Usuário
# 
letra = input('Insira a letra da Palavra Oculta : ').upper()
# Condicional de uma Letra na variavel Resposta
# 
if letra in resposta:
	print('Você acertou a Letra')
else:
	print('Voce errou a Letra')
	#Criada estrutura de repetição
	entrada = input('Digite p para pausar o Programa!!')
	while entrada != 'p':
		print('voce entrou no loop')



