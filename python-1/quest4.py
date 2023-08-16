V1=float(input('Digite o primeiro valor: '))
V2=float(input('Digite o segundo valor: '))
V3=float(input('Digite o terceiro valor: '))

if V1>V2 and V2>V3:
    soma=V1+V2
    print('A soma dos dois maiores valores é de', soma)
if V2>V1 and V1>V3:
    soma=V2+V1
    print('A soma dos dois maiores valores é de', soma)
if V2>V1 and V3>V1:
    soma=V2+V3
    print('A soma dos dois maiores valores é de', soma)
if V3>V1 and V1>V2:
    soma=V3+V1
    print('A soma dos dois maiores valores é de', soma)
