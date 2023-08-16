num=int(input('Digite a quantidade de maçãs compradas: '))

if num<12:
    num*=1.30
    print('O total será de R$'+str(num))
else:
    num*=1
    print('O total será de R$'+str(num))