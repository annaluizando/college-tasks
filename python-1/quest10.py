quant=int(input('Digite a quantidade de frutas compradas: '))
fruta=(input('Digite a fruta comprada [M para Maçã ou MO para Morango]: '))

if fruta=='MO' and quant<=5:
    total=2*quant
    print('O total a ser pago é de R$'+str(total))
elif fruta=='MO' and quant>5:
    total=1.80*quant
    print('O total a ser pago é de R$'+str(total))
elif fruta=='M' and quant<=5:
    total=1.50*quant
    print('O total a ser pago é de R$'+str(total))
elif fruta=='M' and quant>5:
    total=1.10*quant
    print('O total a ser pago é de R${:.2f}'.format(total))
