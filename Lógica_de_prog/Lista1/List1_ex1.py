nome_aluno = input('Informe o nome do(a) aluno(a): ')
nota1 = float(input('Digite o valor da primeira nota: '))
nota2 = float(input('Digite o valor da segunda nota: '))
nota3 = float(input('Digite o valor da terceira nota: '))

media = (nota1 + nota2 + nota3)/3
media = round(media, 2)

print(f'A média das três notas do aluno {nome_aluno.title()} é: {media}')