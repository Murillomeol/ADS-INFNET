n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))


numeros = [n1, n2, n3]
crescente = sorted(numeros)
for num in crescente:
    print (num)