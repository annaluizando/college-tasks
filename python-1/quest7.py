time1=(input('Digite o nome do primeiro time: '))
time2=(input('Digite o nome do segundo time: '))
gol1=(input('Digite o número de gols marcado pelo primeiro time: '))
gol2=(input('Digite o número de gols marcado pelo segundo time: '))

if gol1>gol2:
    print('O time vencedor foi o', time1)
elif gol2>gol1:
    print('O time vencedor foi o', time2)
else:
    print('EMPATE')