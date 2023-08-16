valores=[]
par=[]

continuar=True
while continuar==True:
    N=int(input('Digite um número: '))
    if N==0:
        continuar==False
        break
    valores.append(N)
    if N%2==0:
        par.append(N)
media=sum(par)/len(par)
print('A média dos valores pares é', media)