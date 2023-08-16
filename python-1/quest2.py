sal=float(input('Digite o seu salário mensal: '))
per=float(input('Digite o percentual de reajuste: '))

reaj = sal*(per/100)
novoSal = sal-reaj

print('O salário após o reajuste será: ', novoSal)