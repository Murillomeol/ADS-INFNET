try:
    n1 = float(input("Informe a primeira nota: "))
    n2 = float(input('Informe a segunda nota: '))
    print('A nota foi de', (n1 + n2) / 2)
except:
    print('Falha na conversão')

print(f'\n#AULA 2.')
def calcular_quadrado(num):
    quadrado = num * num
    return quadrado

numero = float(input('Informe um número: '))
quadrado = calcular_quadrado(numero) #chamando a função passando a variável 'numero' como parâmetro.
print('O quadrado de', numero,'é', quadrado)

print(f'\n#AULA 3.')
from datetime import datetime
from time import strftime
import datetime

def boas_vindas(nome):
    print(f'Boas vindas, {nome}.')

boas_vindas(input('Digite seu nome: '))

