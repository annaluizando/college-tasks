valores=[]

for i in range (1, 11):
    valor=int(input("Digite um valor: "))
    valores.append(valor)

media=sum(valores)/len(valores)
print('A média dos valores é', media)