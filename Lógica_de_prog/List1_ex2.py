nota1 = float(input('Digite o valor da primeira nota: '))
nota2 = float(input('Digite o valor da segunda nota: '))
nota3 = float(input('Digite o valor da terceira nota: '))

mediapond = (nota1 * 1 + nota2 * 2 + nota3 * 3) / (1 + 2 + 3)
mediaponde = round(mediapond, 2) #Arredondamentoda média pra printar logo após.

print(f'A média das três notas é: {mediaponde}')