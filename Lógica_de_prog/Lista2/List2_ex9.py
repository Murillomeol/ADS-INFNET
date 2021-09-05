meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

while True:
    mes = int(input('Digite o número referente ao mês do ano: '))
    if mes < 1 or mes > 12:
        print('Entrada inválida.')
    else:
        break

for valor in range(len(meses)):
    if valor + 1 == mes:
        print(f'O mes é {meses[valor]}')