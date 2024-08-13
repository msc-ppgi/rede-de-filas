from PIL import Image
import os
import math

# Função para encontrar todas as imagens em subdiretórios
def encontrar_imagens(diretorio_raiz):
    imagens = []
    for root, dirs, files in os.walk(diretorio_raiz):
        for file in files:
            if file.lower().endswith(".png"):
                caminho_completo = os.path.join(root, file)
                imagens.append(Image.open(caminho_completo))
    return imagens

# Função para juntar imagens em um grid quadrado
def juntar_imagens(imagens):
    n = len(imagens)
    tamanho_grid = math.ceil(math.sqrt(n))
    
    # Calcula o tamanho da célula baseado na primeira imagem (assume-se que todas têm a mesma resolução)
    largura_celula, altura_celula = imagens[0].size
    
    # Cria uma nova imagem grande o suficiente para conter todas as imagens originais
    nova_imagem = Image.new('RGB', (tamanho_grid * largura_celula, tamanho_grid * altura_celula), (255, 255, 255))
    
    for i, imagem in enumerate(imagens):
        x = (i % tamanho_grid) * largura_celula
        y = (i // tamanho_grid) * altura_celula
        nova_imagem.paste(imagem, (x, y))
    
    return nova_imagem

# Diretório raiz onde as imagens estão
diretorio_raiz = "."

# Encontra todas as imagens
imagens = encontrar_imagens(diretorio_raiz)

# Junta as imagens em um grid
imagem_final = juntar_imagens(imagens)

# Salva a imagem final em alta resolução
imagem_final.save("imagem_junta.png", format="PNG")
