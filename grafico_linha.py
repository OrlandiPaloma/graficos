#criar gráfico linha
import matplotlib.pyplot as plt

x = [1, 2, 5]
y = [3, 4, 7]

#Título
plt.title("Gráfico de linha")

#Legendas dos Eixos
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")

plt.plot(x, y) #plot define o tipo de gráfico (linha)
plt.show()

