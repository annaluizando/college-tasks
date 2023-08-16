dia=int(input("Digite o dia em que você nasceu [só o dia]:"))
mes=int(input("Digite o mês em que você nasceu:"))
ano=int(input("Digite o ano em que você nasceu:"))
anoAtual=2022
ageAno=anoAtual-ano-1
diaAtual=20
mesAtual=4
if diaAtual>=dia and mesAtual>=mes:
    age=ageAno+1
else:
    age=ageAno
print("Você tem ", age, " anos.")