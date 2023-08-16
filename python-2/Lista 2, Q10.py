valor=int(input("Digite um valor inteiro entre 1 a 10: "))
if valor<=0:
    print("O valor não pode ser aceito")
for tabuada in range (1, 11):
    if tabuada!=0:
        print(valor*tabuada)