N1=int(input('Digite a primeira nota: '))
N2=int(input('Digite a segunda nota: '))
N3=int(input('Digite a terceira nota: '))
exer=int(input('Digite a média de exercícios: '))

media=(N1+N2*2+N3*3+exer)/7

if media>=9:
    print('Sua média de aproveitamento foi A')
elif media>=7.5 and media<9:
    print('Sua média de aproveitamento foi B')
elif media>=6 and media<7.5:
    print('Sua média de aproveitamento foi C')
elif media<6:
    print('A média de aproveitamento foi D')