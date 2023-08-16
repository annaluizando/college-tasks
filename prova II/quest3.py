sal=float(input('Digite o seu salário: '))
idade=int(input('Digite a sua idade: '))

if idade<=18:
    aumento=sal*(5/100)
    salNovo=sal+aumento
    print('O novo salário será de R$'+str(salNovo))

if 18<idade<60:
    aumento=sal*(10/100)
    salNovo=sal+aumento
    print('O novo salário será de R$'+str(salNovo))

if idade>60:
    aumento=sal*(15/100)
    salNovo=sal+aumento
    print('O novo salário será de R$'+str(salNovo))