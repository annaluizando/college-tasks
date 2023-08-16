litros=float(input('Digite a quantidade de litros comprados: '))
tipo=(input('Digite o tipo de combustível comprado [A para álcool ou G para gasolina]: '))

if tipo=='G' and litros<=20:
    litros*=1.20
    litros=litros-(litros*(4/100))
    print('O total a ser pago é de R$'+str(litros))

elif tipo=='G' and litros>20:
    litros*=1.20
    litros=litros-(litros*(6/100))
    print('O total a ser pago é de R$'+str(litros))

elif tipo=='A' and litros>20:
    litros*=0.90
    litros=litros-(litros*(5/100))
    print('O total a ser pago é de R$'+str(litros))

elif tipo=='A' and litros<=20:
    litros*=0.90
    litros=litros-(litros*(3/100))
    print('O total a ser pago é de R$'+str(litros))
