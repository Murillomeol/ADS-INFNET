salario_atual = float(input('Digite o valor do salário atual: '))
reajuste = float(input('Digite qual é o valor do reajuste em casas decimais: '))

novo_salario = (salario_atual * reajuste) + salario_atual
novo_salario = round(novo_salario, 2)

print(f'O valor do novo salário é de: {novo_salario}')