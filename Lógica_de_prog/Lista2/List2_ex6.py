caracter = input('Digite um caracter: ')
caracter = caracter.lower()

lista = ['a', 'e', 'i', 'o', 'u']

if caracter in lista:
    print('É vogal.')
else:
    print('Não é vogal.')