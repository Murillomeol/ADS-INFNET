primeiro_octeto = int(input('Digite o valor do primeiro octeto: '))

if primeiro_octeto < 0:
    print('Código Inválido.')
elif primeiro_octeto < 128:
    print('Classe A.')
elif primeiro_octeto < 192:
    print('Classe B.')
elif primeiro_octeto < 224:
    print('Classe C.')
elif primeiro_octeto < 240:
    print('Classe D.')
else:
    print('Classe E.')