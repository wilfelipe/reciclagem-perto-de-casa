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
			loc = geolocator.geocode(endereco + ',' + cidade + ',' + estado, addressdetails=True)
			try:
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
	print("------------------------------------------")
	print("MATERIAIS / CIDADE / RUA / COORDENADAS")
	print("------------------------------------------\n\n")

	print("Vidros, Metais, Plásticos e Papéis / Campinas / R. Dante Suriani, 2-382,Chácara Cneo,Ecoponto Jardim / -22.903883,-47.105823\n")
	print("Vidros, Metais, Plásticos e Papéis / Campinas / R. Dr Lázaro Pinto Barroso, 700',Cidade Satélite Íris ,Cooperativa de Trabalho dos Catadores de Materiais Recicláveis / -22.930921,-47.151572\n")
	print("Vidros, Metais, Plásticos e Papéis / Campinas / Av. Santa Isabel, 2300',Barçao Geraldo,Ecoponto Ponto Verde / -22.817622,-47.097850\n")
	print("Vidros, Metais, Plásticos e Papéis / Campinas / R. Saldanha da Gama, 77',Vila Costa e Silva,Ecoponto Vila Costa e Silva / -22.855585,-47.067583\n")
	print("Vidros, Metais, Plásticos e Papéis / Campinas / R. Manoel Gomes Ferreira, 42,Parque Tropical ,Ecoponto Vila União / -22.936055,-47.118054\n")
	print("Vidros, Metais, Plásticos e Papéis / Campinas / Av. Mal. Rondon, ',Jardim Chapadão,Ecoponto Jardim Eulina / -22.892240,-47.100945\n")
	print("Vidros, Metais, Plásticos e Papéis / Campinas / Parque Ecologico Campinas,Parque Ecologico,Ponto Verde Parque Ecológico / -22.899910,-47.019531\n")
	print("Vidros, Metais, Plásticos e Papéis / Campinas / R. Estácio de Sá, 577',Jardim Santa Genebra,Cooperativa de Recicláveis Santa Genebra / -22.851818,-47.075009\n")
	print("Pneus / Campinas / Av. Prefeito Faria Lima, 630 Parque Italia,Descarte de Pneus/Departamento de Limpeza Urbana / -22.915431,-47.071117\n")
	print("Vidros, Metais, Plásticos e Papéis / Campinas / Rua Francisco Theodoro, 1050',Vila Industrial,Região Central / -22.908967,-47.066968\n")
	print("Vidros, Metais, Plásticos e Papéis / Campinas / Rua Celso Soares Colto,Parque Itajaí,Parque Itajaí / -22.961648,-47.192331\n")
	print("Vidros, Metais, Plásticos e Papéis / Campinas / Rua Placida Pretini,Parque São Jorge,Parque São Jorge / -22.895982,-47.157851\n")
	print("Vidros, Metais, Plásticos e Papéis / Campinas / Rua José Martins Lourenço,Jardim Bom Sucesso,Jardim São Gabriel / -22.942435,-47.029831\n")
	print("Vidros, Metais, Plásticos e Papéis / Campinas / Rua dos Cambarás, 200',Vila Boa Vista,Parque via Norte / -22.885794,-47.128180\n")
	print("Vidros, Metais, Plásticos e Papéis / Campinas / Rua Góia Jr.,Res. Parque Rio Das Pedras,Vida Nova /-22.797185,-47.083559\n")
	print("Vidros, Metais, Plásticos e Papéis / Campinas / Avenida São José dos Campos,Parque São Martinho,Vila Campo Sales / -22.946911,-47.055111\n")
	print("Vidros, Metais, Plásticos e Papéis / Campinas / Rua Dom Pedro, 464',Jardim Conceição,Sousas / -22.899055,-46.979964\n\n")
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
