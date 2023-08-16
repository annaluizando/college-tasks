valor=int(input("Digite um valor (entre 1 e 10): "))
if 10<valor or valor<1:
    print("O valor não pode ser aceito")
for tabuada in range(valor, 11):
    if tabuada!=0:
        print(valor*tabuada)