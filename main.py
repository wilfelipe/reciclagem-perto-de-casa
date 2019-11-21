### --- Início da Primeira função, definida como opção número #1 --- ###
import csv
import os
from geopy.distance import geodesic
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="reciclagem-perto-de-casa")

def clear(mensagem):
	os.system('cls')
	print('--------------------', mensagem, '--------------------')

def distancia(coordenadasUsuario, coordenadasPonto):
	return geodesic(coordenadasUsuario, coordenadasPonto).miles * 1.609

def pontoColetaNearMe():
	modoPesquisa = 'endereco'
	erro = False
	while True:
		clear('O que você deseja reciclar?')
		try:
			choice = int(input("1. Vidros\n2. Metais\n3. Plásticos\n4. Pneus\n5. Papéis\n\nDigite uma opção: "))
		except:
			pass
		else:
			if choice == 1:
				produto = 'Vidros'
				break
			elif choice == 2:
				produto = 'Metais'
				break
			elif choice == 3:
				produto = 'Plasticos'
				break
			elif choice == 4:
				produto = 'Pneus'
				break
			elif choice == 5:
				produto = 'Papeis'
				break
	while True:
		clear('Qual o seu endereço?')
		if modoPesquisa == 'endereco':
			cidade = input('Cidade: ')
			estado = input('Estado: ')
			endereco = input('Endereço: ')
			try:
				loc = geolocator.geocode(endereco + ',' + cidade + ',' + estado, addressdetails=True)
				coordenadasUsuario = [loc.latitude, loc.longitude]
			except:
				erro = True
			else:
				break
		else:
			try:
				coordenadasUsuario = [float(input('Digite sua latitude (Exemplo: -22.9006708): ')), float(
				input('Digite sua longitude (Exemplo: -47.1672872): '))]  # Entrada das coordenadas do usuário
			except:
				erro = True
			else:
				break
		if erro:
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
			coordenadasPonto = [float(row[5]), float(row[6])]
			if produto in row[0].split(','):
				pontosColeta.append([distancia(coordenadasUsuario, coordenadasPonto), row[0], row[1], row[2], row[3], row[4], row[5]]) # Adicionando a distância do ponto de coleta para o usuário mais os dados desse ponto, para a matriz pontosColeta
		pontosColeta.sort() # Organizando lista pela distância, gerada pela função distancia, do mais próximo ao mais distante.

		# ----- Mostrando resultados para o usuário ----
		n = 3  # Número de resultados que serão apresentados
		if len(pontosColeta) < n:
			n = len(pontosColeta)
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
	print("Feito por Alejandro   de   Oliveira   Montes - RA:F0460B-3")
	print("Feito por Igor   Carvalho   Tavares  - RA:N39088-3 ")
	print("Feito por Roger - RA:F1281f-0")
	print("Feito por Thiago M. Nóbrega - RA:F028BF-2")
	print("Feito por Wilson   Felipe   Martins   Carvalho - RA:N472BJ-7 \n")
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

