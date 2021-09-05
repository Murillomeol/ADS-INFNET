raio = float(input('Digite o raio da caixa d\'água: '))
altura = float(input('Digite o valor da altura da caixa d\'água: '))
pi = 3.14159265358979324

volume = pi * raio ** 2 * altura
volume = round(volume,2)

print(volume)