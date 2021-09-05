salário = float(input('Digite o salário atual: '))

if salário <= 1000:
    salário = salário + (salário * 0.3)
    print(f'O novo salário é {salário}.')
elif salário <= 2000:
    salário = salário + (salário * 0.25)
    print(f'O novo salário é {salário}.')
elif salário <= 3000:
    salário = salário + (salário * 0.2)
    print(f'O novo salário é {salário}.')
elif salário <= 4000:
    salário = salário + (salário * 0.15)
    print(f'O novo salário é {salário}.')
else:
    salário = salário + (salário * 0.1)
    print(f'O novo salário é {salário}.')