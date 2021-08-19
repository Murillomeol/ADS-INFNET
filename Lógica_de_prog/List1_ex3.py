altura = float(input('Digite o valor da altura em metros: '))
peso = float(input('DIgite o peso em kilogramas: '))

imc = peso / altura ** 2
imc = round(imc, 2)

print(f'O IMC desta pessoa é {imc}')