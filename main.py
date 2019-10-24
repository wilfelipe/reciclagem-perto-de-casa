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
	coordenadasUsuario = [radians(coordenadasUsuario[0]), radians(coordenadasUsuario[1])]  # Convertendo valores de graus para radiano
	coordenadasPonto = [radians(coordenadasPonto[0]), radians(coordenadasPonto[1])]  # Convertendo valores de graus para radiano
	# Delta da latitude entre os dois pontos
	dlat = coordenadasUsuario[0] - coordenadasPonto[0]
	# Delta da longitude entre os dois pontos
	dlon = coordenadasUsuario[1] - coordenadasPonto[1]

	# ----- Formula Haversine ----
	a = sin(dlat/2)**2 + \
	cos(coordenadasUsuario[0]) * cos(coordenadasPonto[0]) * sin(dlon/2)**2
	c = 2 * asin(sqrt(a))
	# ----- Formula Haversine ----

	R = 6371  # Raio da terra em Km

	return c * R  # Retornando a distância em Kilômetros entre os dois pontos.

def pontoColetaNearMe():
	while True:
		clear('Ponto de coleta mais próximo de você')
		try:
			coordenadasUsuario = [float(input('Digite sua latitude (Exemplo: -22.9006708): ')), float(input('Digite sua longitude (Exemplo: -47.1672872): '))] # Entrada das coordenadas do usuário
		except ValueError:
			pass
		else:
			break

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
			coordenadasPonto = [float(row[5]), float(row[6])] # Convertendo valores latitude e longitude de str para float, para que possa ser feito operações matemáticas

			pontosColeta.append([haversine(coordenadasUsuario, coordenadasPonto),row[0],row[1],row[2],row[3],row[4],row[5]]) # Adicionando a distância do ponto de coleta para o usuário mais os dados desse ponto, para a matriz pontosColeta

			pontosColeta.sort() # Organizando lista pela distância, gerada pela função haversine, do mais próximo ao mais distante.

			# pontosColeta[x][0] = Distância do ponto para o usuário, em Km.
			# pontosColeta[x][1] = Tipos de residuos
			# pontosColeta[x][2] = Bairro
			# pontosColeta[x][3] = Endereço
			# pontosColeta[x][4] = Complemento
			# pontosColeta[x][5] = Observação

		# ----- Mostrando resultados para o usuário ----
		n = 3 # Número de resultados que serão apresentados
		clear('Pontos de coleta mais próximo de você')
		for i in range(n):
			print(pontosColeta[i][5])
			print('Distância: ', round(pontosColeta[i][0], 2), 'Km')
			print('Enderço: ', pontosColeta[i][3], '.', pontosColeta[i][2])
			print('Tipos de residuos: ', pontosColeta[i][1])
			print('---------------------------')
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
	print("Para ver qual o ponto de coleta mais próximo de você, digite '1'")
	print("Para ver todos os locais que você pode reciclar, digite '2'")
	print("Para cadastrar algum ponto de coleta que você conhece, digite '3'")
	print("Para você ver quem criou esse projeto, digite '4'" )
	print("Para sair, digite '5'" )
	
	try:
		choice = int(input("\nQual a sua escolha? (1, 2, 3, 4 ou 5?): "))
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
