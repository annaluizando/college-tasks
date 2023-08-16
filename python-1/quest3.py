anoAtual=int(input('Digite o ano atual: '))
anoNasc=int(input('Digite o seu ano de nascimento: '))

if anoAtual-anoNasc>=18:
    print('Você poderá votar esse ano.')
else:
    print('Você não poderá votar esse ano.')