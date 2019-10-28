from math import radians, cos, sin, asin, sqrt
import csv
import os


def clear(mensagem):
	os.system('cls')
	print('--------------------', mensagem, '--------------------')


'''
	Essa função recebe recebe duas listas como parâmetro, a primeira lista contendendo as coordenadas digita pelo usuário, e a segunda as coordenas do ponto de coleta, onde o primeiro elemento da lista é a latitude e o segundo elemento a longitude. A função retorna a distância, em kilometros entre a localização do usuário e a localização do ponto de coleta. 
'''


def haversine(coordenadasUsuario, coordenadasPonto):
	coordenadasUsuario = [radians(coordenadasUsuario[0]), radians(
		coordenadasUsuario[1])]  # Convertendo valores de graus para radiano
	coordenadasPonto = [radians(coordenadasPonto[0]), radians(
		coordenadasPonto[1])]  # Convertendo valores de graus para radiano
	# Delta da latitude entre os dois pontos
	dlat = coordenadasUsuario[0] - coordenadasPonto[0]
	# Delta da longitude entre os dois pontos
	dlon = coordenadasUsuario[1] - coordenadasPonto[1]

	# ----- Formula Haversine ----
	a = sin(dlat/2)**2 + \
            cos(coordenadasUsuario[0]) * \
            cos(coordenadasPonto[0]) * sin(dlon/2)**2
	c = 2 * asin(sqrt(a))
	# ----- Formula Haversine ----

	R = 6371  # Raio da terra em Km

	return c * R  # Retornando a distância em Kilômetros entre os dois pontos.


def pontoColetaNearMe():
	while True:
		clear('Ponto de coleta mais próximo de você')
		try:
			coordenadasUsuario = [float(input('Digite sua latitude (Exemplo: -22.9006708): ')), float(
				input('Digite sua longitude (Exemplo: -47.1672872): '))]  # Entrada das coordenadas do usuário
		except ValueError:
			pass
		else:
			break
	# Pedindo para o usuario o ele deseja que seja mostrado na tela
	escolhas = []  # armazena as opções
	n = 0
	while n < 1:
		clear(" ")
		print("Para ver a distância entre seu endereço e o ecoponto, digite '1'")
		print("para ver os tipos de residuos aceitos pelo ecoponto, digite '2'")
		print("Para ver o bairro em que está localizado o ecoponto, digite '3'")
		print("Para ver o endereço em que está localizado o ecoponto, digite '4'")
		print("Para ver o Complemento do endereço do ecoponto, digite '5'")
		print("Para ver as observações referentes ao ecoponto, digite '6'")
		a = int(input("Caso queira parar de adicionar opções, digite um número negativo\n"))
		if a > 0 and a < 8:
			escolhas.append(a)
		else:
			n += 1
	n = 0
	# Abrindo dataset com todos os pontos de coleta na região de Recife
	with open('pontos-de-coletas-residuos.csv', encoding="utf8") as f:
		reader = csv.reader(f)

		'''
			Lendos todas as linhas contidas na tabela 'pontos-de-coletas-residuos.csv'. Esse for irá agregar cada linha da tabela a váriabel row.
			Caso a tabela tenha 25 linhas, o código irá passar pelo for 25 vezes e em cada vez a variável row será uma lista com os valores daquela coluna x linha.
			row = [tiposresiduos, bairro, endereco, complemento, observacao, latitude, longitude
		'''
		pontosColeta = []
		# Row[0] = Tipos de residuos
		# Row[1] = Bairro
		# Row[2] = Endereço
		# Row[3] = Complemento
		# Row[4] = Observação
		# Row[5] = Latitude do ponto de coleta
		# Row[6] = Longitude do ponto de coleta
		for row in reader:
			# Convertendo valores latitude e longitude de str para float, para que possa ser feito operações matemáticas
			coordenadasPonto = [float(row[5]), float(row[6])]

			# Adicionando a distância do ponto de coleta para o usuário mais os dados desse ponto, para a matriz pontosColeta
			pontosColeta.append([haversine(coordenadasUsuario, coordenadasPonto),
                            row[0], row[1], row[2], row[3], row[4], row[5]])

			# Organizando lista pela distância, gerada pela função haversine, do mais próximo ao mais distante.
			pontosColeta.sort()

			# pontosColeta[x][0] = Distância do ponto para o usuário, em Km.
			# pontosColeta[x][1] = Tipos de residuos
			# pontosColeta[x][2] = Bairro
			# pontosColeta[x][3] = Endereço
			# pontosColeta[x][4] = Complemento
			# pontosColeta[x][5] = Observação

		# ----- Mostrando resultados para o usuário ----
		n = 3  # Número de resultados que serão apresentados
		clear('Pontos de coleta mais próximo de você')
		b = len(escolhas)
		y = 0
		for i in range(n):
			"""
			print(pontosColeta[i][5])
			print('Distância: ', round(pontosColeta[i][0], 2), 'Km')
			print('Enderço: ', pontosColeta[i][3], '.', pontosColeta[i][2])
			print('Tipos de residuos: ', pontosColeta[i][1])
			print('---------------------------')
			"""
			while y < b:
				if escolhas[y] == 1:
					print('Distância: ', round(pontosColeta[i][0]), 'Km', end='   ')
				elif escolhas[y] == 2:
					print('Tipos de residuos: ', pontosColeta[i][1], end="   ")
				elif escolhas[y] == 3:
					print('Bairro: ', pontosColeta[i][2], end="   ")
				elif escolhas[y] == 4:
					print('Endereço: ', pontosColeta[i][3], end="   ")
				elif escolhas[y] == 5:
					print('Complemento: ', pontosColeta[i][4], end="   ")
				elif escolhas[y] == 6:
					print('Observação: ', pontosColeta[i][5], end="   ")
				print("\n")
				y += 1
			print("\n--------------------------------------------------\n")
			y = 0
		# ----- Mostrando resultado para o usuário ----
		input('Pressione ENTER para continuar...')


def allPontos():
	pass


def sobre():
	pass


def cadastrarPonto():
	pass


while True:
	clear("Reciclagem Perto de Casa")
	try:
		choice = int(input("\n1. Ponto de coleta mais próximo\n2. Todos pontos de coleta\n3. Cadastrar ponto de coleta\n4. Sobre nós\n5. Sair\n\nDigite uma opção: "))
	except:
		pass
	else:
		if choice == 1:
			pontoColetaNearMe()
		elif choice == 2:
			allPontos()
		elif choice == 3:
			cadastrarPonto()
		elif choice == 4:
			sobre()
		elif choice == 5:
			exit()
