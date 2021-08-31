print(f'\n#AULA 6 - Booleanos')
print('uva' > 'macã')
print('\n')

def voto_obrigatorio(idade):
    return idade >= 18 and idade < 70

print(f'{voto_obrigatorio(54)}')

def voto_facultativo(idade):
    return idade >= 70 or (idade >= 16 and idade < 18)

print(f'{voto_facultativo(70)}')