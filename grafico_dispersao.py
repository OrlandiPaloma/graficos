#criar gráfico barra
import matplotlib.pyplot as plt

x = [1, 3, 5, 7, 9]
y = [2, 3, 7, 1, 2]

titulo = "Gráfico de dispersão: Scatterplot"
eixox = "Eixo X"
eixoy = "Eixo Y"

#Legendas
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)

plt.scatter(x, y, label = "Meus pontos", color = "g", marker = ".", s = 150)  #Grafico de dispersão. Label é referente a legenda. 
#Color altera as cores dos pontos e marker altera o tipo de marcador.
#S altera o tamanho do marcador.

plt.plot(x, y, color = "black", linestyle="-") #Criação de linhas para ligar os pontos do scatter. Color altera a cor da linha
plt.legend() #Para imprir legenda

plt.show() #Para imprimir o gráfico
#plt.savefig("Figura1.png") #Para salvar o gráfico/figura