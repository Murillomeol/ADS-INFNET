def diagnosticar_situacao_eleitoral(idade):
    if idade >= 18 and idade < 70:
        print('Voto obrigatório.')
    elif idade >= 16:
        print('Voto facultativo.')
    else:
        print('Não pode votar.')

diagnosticar_situacao_eleitoral(50)
diagnosticar_situacao_eleitoral(90)
diagnosticar_situacao_eleitoral(12)
diagnosticar_situacao_eleitoral(16)