import csv
import matplotlib.pyplot as plt
from datetime import datetime

# Substitua 'seu_arquivo.csv' pelo caminho do seu arquivo CSV
caminho_arquivo = 'C:\\Users\\vitor\\Desktop\influx.data.csv'
print(caminho_arquivo)
valores_colunas = []
with open(caminho_arquivo, mode='r', encoding='utf-8') as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv)
    # Pula os cabeçalhos e as três primeiras linhas de dados
    next(leitor_csv)  # Cabeçalhos
    next(leitor_csv)  # Primeira linha
    next(leitor_csv)  # Segunda linha
    next(leitor_csv)  # Segunda linha
    for linha in leitor_csv:
        # Seleciona os valores das colunas 6 e 13
        if linha != []:
            valor_coluna_5 = linha[5]
            valor_coluna_6 = linha[6]
            valor_coluna_13 = linha[13]
            # Adiciona o par de valores à lista
            valores_colunas.append([valor_coluna_5, valor_coluna_6, valor_coluna_13])

dados = sorted(valores_colunas, key=lambda x: datetime.fromisoformat(x[0].replace('Z', '')))



# Inicializa listas para x e y
x_hello = []
y_hello = []
x_hello_error = []
y_hello_error = []

# Itera sobre os dados e popula as listas
for i, (timestamp, valor, tipo) in enumerate(dados):
    if tipo == 'hello':
        x_hello.append(i + 1)  # Sequência numérica começando em 1
        y_hello.append(int(valor))
    elif tipo == 'hello.error':
        x_hello_error.append(i + 1)  # Sequência numérica começando em 1
        y_hello_error.append(int(valor))

# Cria o gráfico de linha
plt.plot(x_hello, y_hello, color='blue', label='hello', marker='o')
plt.plot(x_hello_error, y_hello_error, color='red', label='hello.error', marker='x')

# Adiciona títulos e rótulos
plt.title('Gráfico de Linha de hello e hello.error')
plt.xlabel('Tempo (sequência numérica)')
plt.ylabel('Valor')

# Adiciona a legenda
plt.legend()

# Exibe o gráfico
plt.show()

