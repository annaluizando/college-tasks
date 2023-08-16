litros=float(input('Digite quantos litros foram comprados: '))
tipoC=str(input('Digite o tipo de combustível comprado [A ou G]: '))
if tipoC=='A' and litros<=20:
    total=(litros*0.90) - (litros*3)/100
    print('O total a ser pago pelo cliente é de R$', total)
if tipoC=='A' and litros>20:
    total=(litros*0.90) - (litros*5)/100
    print('O total a ser pago pelo cliente é de R$', total)
if tipoC=='G' and litros<=20:
    total=(litros*1.20) - (litros*4)/100
    print('O total a ser pago pelo cliente é de R$', total)
if tipoC=='G' and litros>20:
    total=(litros*1.20) - (litros*6)/100
    print('O total a ser pago pelo cliente é R$', total)