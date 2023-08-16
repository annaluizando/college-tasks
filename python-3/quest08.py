valores=[]

for i in range (1,51):
    valor=int(input('Digite um valor: '))
    valores.append(valor)
print('O menor valor é {} e o maior valor é {}'.format(min(valores), max(valores)))