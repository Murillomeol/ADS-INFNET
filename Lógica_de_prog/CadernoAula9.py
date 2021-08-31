x = 0
while x < 6:
    x += 1
    if x % 2 == 1:
        continue

    print(f'O valor é {x}')
    print(f'O quadrado de {x} é {x ** 2}')
    print(f'A raiz quadrada de {x} é {x ** 0.5}')
    print(f'\n\n')

import random

while True:
    numero = random.randint(0,5)
    palpite = int(input('Tente adivinhar um número de 0 a 5: '))
    if palpite == numero:
        print('Acertou!')
        break
    else:
        print(f'Errou! O número era: {numero}')
print(f'\n')

import time

while True:
    print('Se quer falar sobre internet, digite 1.')
    time.sleep(2)
    print('Se quer falar sobre TV a cabo, digite 2.')
    time.sleep(2)
    print('Se quer encerrar seu atendimento, digite 0.')
    opção = int(input('Digite a opção desejada: '))
    if opção == 0:
        print(f'Você digitou {opção}. Agradecemos pelo seu contato!')
        break
    elif opção == 1:
        print(f'Você digitou {opção}, vamos te encaminhar para um de nossos atendentes para falar sobre internet.')
        break
    elif opção == 2:
        print(f'Você digitou {opção}, vamos te encaminhar para um de nossos atendentes para falar sobre TV a cabo.')
        break
    else:
        print(f'{opção} não é uma opção válida.\n')
        