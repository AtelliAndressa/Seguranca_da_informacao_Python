import phonenumbers  # fornece informações de um num de telefone, validação e etc..
from phonenumbers import geocoder # vai trazer a localização


phone = input('Digite o telefone no formato +551140028922:  ')
phone_numbers = phonenumbers.parse(phone) # string passada no input vai ser convertida para numero de telefone aqui
print(geocoder.description_for_number(phone_numbers, 'pt')) # vai mostrar a localização em português



