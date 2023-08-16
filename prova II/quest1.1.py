contagem=[]

num = 0
while num<20:
    if num % 2 == 0:
        contagem.append(num)
    num += 1
print('Os números pares são: ', contagem)