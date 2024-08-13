import os
import pandas as pd



# Lista para armazenar os resultados
results = []

# Navegue pelos subdiretórios
for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith('.csv'):
            # Caminho completo do arquivo CSV
            file_path = os.path.join(root, file)
            
            # Leia o arquivo CSV
            df = pd.read_csv(file_path)
            
            # Calcule a média da coluna 'X'
            mean_x = df['X'].mean()
            
            # Obtenha o nome do subdiretório (pasta)
            folder_name = os.path.basename(root)
            
            # Adicione o resultado à lista
            results.append({'nome da pasta': folder_name, 'Mean X': mean_x})

# Crie um DataFrame com os resultados
results_df = pd.DataFrame(results)

# Salve os resultados em um novo arquivo CSV
results_df.to_csv('mean_x_results.csv', index=False)

print('Médias calculadas e salvas em mean_x_results.csv')
