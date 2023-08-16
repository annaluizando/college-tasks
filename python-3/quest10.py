num=[]
par=[]

continuar=True

while continuar==True:
    N=int(input('Digite um número positivo: '))
    if N<0:
        print('O número digitado deve ter valor maior que zero.')
    elif N==0:
        continuar=False
        break
    num.append(N)
    if (N%2)==0:
        par.append(N)
print('Os números pares entre os digitados são: ', par)

