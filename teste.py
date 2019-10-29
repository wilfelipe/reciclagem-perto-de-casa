from geopy.geocoders import Nominatim
from geopy.distance import geodesic
geolocator = Nominatim(user_agent="reciclagem-perto-de-casa")


cidade = input('Cidade: ')
estado = input('Estado: ')
endereco = input('Endereço: ')
loc = geolocator.geocode(endereco + ',' + cidade + ',' + estado, addressdetails=True)

print("latitude is:" ,loc.latitude,"\nlongtitude is:" ,loc.longitude)

print(loc.raw['address']['road'] + ', ' + loc.raw['address']['suburb'] + '. ' + loc.raw['address']['city'] + ' - ' + loc.raw['address']['state'] + '. ' + loc.raw['address']['postcode'])


location = geolocator.reverse(str(loc.latitude) + ","  +  str(loc.longitude))
print(location.address)
