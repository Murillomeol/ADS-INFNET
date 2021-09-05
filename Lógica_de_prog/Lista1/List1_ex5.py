preco = float(input('Digite o valor do preço do litro da combustível: '))
valor = float(input('Digite o valor a ser abastecido: '))

litros_abastecidos = valor / preco
litros_abastecidos = round(litros_abastecidos, 2)

print(f'A quantidade de litros abastecidos foi: {litros_abastecidos}')