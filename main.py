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


# Coordenadas simulando dados digitado pelo usuário
coordenadasUsuario = [-8.038874, -34.9330603]


# Abrindo dataset com todos os pontos de coleta na região de Recife
with open('pontos-de-coletas-residuos.csv', encoding="utf8") as f:
	reader = csv.reader(f)

	'''
		Lendos todas as linhas contidas na tabela 'pontos-de-coletas-residuos.csv'. Esse for irá agregar cada linha da tabela a váriabel row.
		Caso a tabela tenha 25 linhas, o código irá passar pelo for 25 vezes e em cada vez a variável row será uma lista com os valores daquela coluna x linha.
		row = [tiposresiduos, bairro, endereco, complemento, observacao, latitude, longitude
	'''
	Menor_Distancia = 20037500
	lista = []
	for row in reader:
		# Convertendo valores latitude e longitude de str para float, para que possa ser feito operações matemáticas
		coordenadasPonto = [float(row[5]), float(row[6])]
		lista.append(
                    [haversine(coordenadasUsuario, coordenadasPonto), row[0], row[1], row[2], row[3], row[4], row[5], row[6]])
		'''
		if Menor_Distancia > haversine(coordenadasUsuario,coordenadasPonto):
			Menor_Distancia = haversine(coordenadasUsuario,coordenadasPonto)
			endereco = row[2]
		'''
		# Row[0] = Tipos de residuos
		# Row[1] = Bairro
		# Row[2] = Endereço
		# Row[3] = Complemento
		# Row[4] = Observação
		# Row[5] = Latitude do ponto de coleta
		# Row[6] = Longitude do ponto de coleta
		'''
			haversine(coordernada1, coordernada2) retorna a distância entre o ponto 1 e o ponto 2.
			Ex: distancia = haversine(coordenadasUnip, coordenadasExtra)
				print(distancia)
				>>> 0.25645
		'''
lista.sort()
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])
print(lista[4])
input()
