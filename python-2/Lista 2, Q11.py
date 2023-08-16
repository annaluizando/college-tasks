salarios=[]
filhos=[]
continuar=True

while continuar==True:
    sal=float(input("Digite seu salário: "))
    if sal<0:
        continuar=False
        break
    salarios.append(sal)
    filho=int(input("Digite quantos filhos você tem "))
    filhos.append(filho)

mediaSal=sum(salarios)/len(salarios)
print("A média salarial é ", mediaSal)
mediaFilhos=sum(filhos)/len(filhos)
print("A média do número de filhos é ", mediaFilhos)

salario100=[]
for salario in salarios:
    if salario<=100:
        salario100.append(salario)
percentual=len(salario100)*100/len(salarios)
print("O percentual de pessoas com salário até R$100 é de", percentual+"%")