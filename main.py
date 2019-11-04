### --- Início da Primeira função, definida como opção número #1 --- ###
from math import radians, cos, sin, asin, sqrt
import csv
import os
from geopy.distance import geodesic
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="reciclagem-perto-de-casa")

def clear(mensagem):
	os.system('cls')
	print('--------------------', mensagem, '--------------------')


'''
	Essa função recebe recebe duas listas como parâmetro, a primeira lista contendendo as coordenadas digita pelo usuário, e a segunda as coordenas do ponto de coleta, onde o primeiro elemento da lista é a latitude e o segundo elemento a longitude. A função retorna a distância, em kilometros entre a localização do usuário e a localização do ponto de coleta. 
'''
def distancia(coordenadasUsuario, coordenadasPonto):
	return geodesic(coordenadasUsuario, coordenadasPonto).miles * 1.609


def pontoColetaNearMe():
	modoPesquisa = 'endereco'
	erro = 0
	while True:
		clear('Ponto de coleta mais próximo de você')
		if modoPesquisa == 'endereco':
			cidade = input('Cidade: ')
			estado = input('Estado: ')
			endereco = input('Endereço: ')
			try:
				loc = geolocator.geocode(endereco + ',' + cidade + ',' + estado, addressdetails=True)
				coordenadasUsuario = [loc.latitude, loc.longitude]
			except:
				erro = 1
			else:
				break
		else:
			try:
				coordenadasUsuario = [float(input('Digite sua latitude (Exemplo: -22.9006708): ')), float(
				input('Digite sua longitude (Exemplo: -47.1672872): '))]  # Entrada das coordenadas do usuário
			except:
				erro = 1
			else:
				break

		if erro == 1:
			clear("ERRO! Não encontramos seu endereço")
			try:
				choice = int(input("1. Tentar novamente\n2. Procurar usando coordenadas\n\nDigite uma opção: "))
			except:
				pass
			else:
				if choice == 1:
					modoPesquisa = 'endereco'
				else:
					modoPesquisa = 'coordenadas'
				erro = 0
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
			pontosColeta.append([distancia(coordenadasUsuario, coordenadasPonto), row[0], row[1], row[2], row[3], row[4], row[5]])
			# Organizando lista pela distância, gerada pela função distancia, do mais próximo ao mais distante.
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

		for i in range(n):
			print(pontosColeta[i][5])
			print('Distância: ', round(pontosColeta[i][0], 2), 'Km')
			print('Enderço: ', pontosColeta[i][3], '.', pontosColeta[i][2])
			print('Tipos de residuos: ', pontosColeta[i][1])
			print('---------------------------')
		# ----- Mostrando resultado para o usuário ----
		input('Pressione ENTER para continuar...')
### --- Fim da Primeira função, definida como opção número #1 --- ###


### --- Inicio da Função que mostra todos os locais disponiveis para reciclagem --- ###
def allPontos():
	with open('pontos-de-coletas-residuos.csv', encoding="utf8") as f:
		reader = csv.reader(f)
		clear('Todos pontos de coleta cadastrado')
		for row in reader:
			print(row[4])
			print('Enderço: ', row[2], '.', row[3])
			print('Tipos de residuos: ', row[0])
			print('---------------------------')
		input('Pressione ENTER para continuar...')
### --- FIm da Função que mostra todos os locais disponiveis para reciclagem --- ###


### --- Inicio da função sobre --- ###
def sobre():
	clear('Sobre Nós')
	print("Feito por Alejandro Montes - RA:")
	print("Feito por Igor Carvalho - RA: ")
	print("Feito por Roger - RA: ")
	print("Feito por Thiago M. Nóbrega - RA:F028BF-2")
	print("Feito por Wilson Felipe - RA: \n")
	input('Pressione ENTER para continuar...')
### --- Fim da função sobre --- ###


### --- Inicio do Menu --- ###
while True:
	clear("Reciclagem Perto de Casa")
	try:
		choice = int(input("\n1. Ponto de coleta mais próximo\n2. Todos pontos de coleta\n3. Sobre nós\n4. Sair\n\nDigite uma opção: "))
	except:
		pass
	else:
		if choice == 1:
			pontoColetaNearMe()
		elif choice == 2:
			allPontos()
		elif choice == 3:
			sobre()
		elif choice == 4:
			exit()
### --- Fim do Menu --- ###
