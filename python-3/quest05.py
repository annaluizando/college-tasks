valores=[]
inter=[]

for i in range (1, 11):
    valor=int(input('Digite um valor: '))
    valores.append(valor)
    if 10<valor<20:
        inter.append(valor)

print('Os valores entre 10 e 20 são:', len(inter))