#criar gráfico barra
import matplotlib.pyplot as plt

x1 = [1, 3, 5, 7, 9]
y1 = [2, 3, 7, 1, 2]

x2 = [2, 4, 6, 8, 10]
y2 = [5, 1, 3, 7, 4]

titulo = "Gráfico de barras 2"
eixox = "Eixo X"
eixoy = "Eixo Y"

#Legendas
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)

plt.bar(x1, y1, label = 'Grupo 1') #bar define o tipo de gráfico (barra)
plt.bar(x2, y2, label = 'Grupo 2') #label são as legendas de cada grupo de barras
plt.legend() #plotar as legendas para o grafico

plt.show()
