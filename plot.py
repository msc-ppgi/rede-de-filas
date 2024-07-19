import csv
import matplotlib.pyplot as plt

# Leitura do arquivo CSV
x = []
y = []

with open('pontos.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Pular o cabeçalho
    for row in reader:
        x.append(float(row[0]))  # Converter para float
        y.append(float(row[1]))  # Converter para float

# Plotando os pontos
plt.plot(y, x, 'o-')  # 'o-' para pontos conectados por linhas
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Gráfico de Pontos')
plt.show()
