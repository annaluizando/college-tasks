V1=float(input('Digite o primeiro valor: '))
V2=float(input('Digite o segundo valor: '))
V3=float(input('Digite o terceiro valor: '))

if V3<V1+V2 and V2<V3+V1 and V1<V2+V3:
    print('Forma um triângulo')
else:
    print('Não forma um triângulo')