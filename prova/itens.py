while True:
    quantItem=int(input('Digite a quantidade de itens comprados: '))
    if quantItem==0:
        break
    valores=float(input('Digite o seu valor: '))
    formPag=str(input('Digite a forma de pagamento [ a vista ou crédito]: '))
    if formPag=='credito':
        total=(valores*quantItem)-(2/100)
        print('O total é R${}, a quantidade total de itens foi {} e seus valores são {}'.format(total, quantItem, valores))
    if formPag=='a vista':
        total=(valores*quantItem)-(5/100)
        print('O total é R${}, a quantidade total de itens foi {} e seus valores são {}'.format(total, quantItem, valores))