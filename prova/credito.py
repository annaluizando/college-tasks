valores=[]
itens=[]
quantInds=[]
continuar=True

while continuar==True:
    item=str(input('Digite o item comprado: '))
    if item=='0':
        continuar=False
        break
    itens.append(item)
    valor=float(input('Digite o seu valor: '))
    valores.append(valor)
    quantInd=int(input('Digite a quantidade comprada desse item: '))
    quantInds.append(quantInd)
formaP=str(input('Digite a forma de pagamento [a vista ou crédito]: '))

quantTotal=sum(quantInds)

if formaP=='a vista':
    totalF=sum(valores) - (sum(valores) * 5/100)
    print('O total a ser pago é {}, a quantidade total de itens foi {} e seus valores são {}'.format(totalF, quantTotal, valores))
if formaP=='crédito':
    totalF=sum(valores) - (sum(valores) * 2/100)
    print('O total a ser pago é {}, a quantidade total de itens foi {} e seus valores são {}'.format(totalF, quantTotal, valores))