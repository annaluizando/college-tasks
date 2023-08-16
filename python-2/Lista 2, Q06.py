centroX=int(input("Digite as coordenadas X do centro do círculo: "))
centroY=int(input("Digite as coordenadas Y do centro do círculo: "))
raio=int(input("Digite o raio do círculo: "))
pontoX=int(input("Digite o ponto x: "))
pontoY=int(input("Digite o ponto y: "))
distancia=(centroX-pontoX)**2+(centroY+pontoY)**2
if (distancia<raio**2):
    print("O ponto se encontra dentro do círculo")
if (distancia==raio**2) or (distancia>raio**2):
    print("O ponto se encontra fora do círculo")