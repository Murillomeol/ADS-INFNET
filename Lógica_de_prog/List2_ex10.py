
dia = int(input('Digite o dia: '))
mes = int(input('Digite o mês: '))
ano = int(input('Digite o ano: '))

def ano_bissexto (ano):
    if ano % 4 == 0:
        return True
    elif ano % 100 == 0 and ano % 4 == 0:
        return True
    else:
        return False

mes = [range(1,13)]
for m in mes:
    print(f'O mes é {mes(m)}')



for mess in mes:
    if mess in mes == [1, 3, 5, 7, 8, 10, 12]:
        dia < 32
    elif mess in mes == [4, 6, 9, 11]:
        dia < 31
    elif mess in mes == [2]:
        if ano_bissexto(ano):
            dia < 30
        elif ano_bissexto(ano):
            dia < 29


print(f'A data {dia}/{mes}/{ano} é válida.')



