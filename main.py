from math import radians, cos, sin, asin, sqrt
import csv


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
      cos(coordenadasUsuario[0]) * cos(coordenadasPonto[0]) * sin(dlon/2)**2
  c = 2 * asin(sqrt(a))
  # ----- Formula Haversine ----

  R = 6371  # Raio da terra em Km

  return c * R  # Retornando a distância em Kilômetros entre os dois pontos.



coordenadasUsuario = [float(input('Digite sua latitude: ')), float(input('Digite sua longitude: '))] # Entrada das coordenadas do usuário


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
		'''
			haversine(coordernada1, coordernada2) retorna a distância entre o ponto 1 e o ponto 2.
			Ex: distancia = haversine(coordenadasUnip, coordenadasExtra)
				print(distancia)
				>>> 0.25645
		'''
		
pontosColeta.sort() # Organizando lista pela distância, gerada pela função haversine, do mais próximo ao mais distante.

# pontosColeta[x][0] = Distância do ponto para o usuário, em Km.
# pontosColeta[x][1] = Tipos de residuos
# pontosColeta[x][2] = Bairro
# pontosColeta[x][3] = Endereço
# pontosColeta[x][4] = Complemento
# pontosColeta[x][5] = Observação

# ----- Imprindo resultado para o usuário ----
n = 3 # Número de resultados que serão imprimidos
print('\nPontos de coleta mais próximo de você:\n')
for i in range(n):
	print(pontosColeta[i][5])
	print('Distância: ', round(pontosColeta[i][0], 2), 'Km')
	print('Enderço: ', pontosColeta[i][3], '.', pontosColeta[i][2])
	print('Tipos de residuos: ', pontosColeta[i][1])
	print('---------------------------')
input()