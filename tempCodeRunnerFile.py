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
def juntar_imagens(imagens, tamanho_celula):
    n = len(imagens)
    tamanho_grid = math.ceil(math.sqrt(n))
    nova_imagem = Image.new('RGB', (tamanho_grid * tamanho_celula, tamanho_grid * tamanho_celula), (255, 255, 255))
    
    for i, imagem in enumerate(imagens):
        imagem_resized = imagem.resize((tamanho_celula, tamanho_celula))
        x = (i % tamanho_grid) * tamanho_celula
        y = (i // tamanho_grid) * tamanho_celula
        nova_imagem.paste(imagem_resized, (x, y))
    
    return nova_imagem

# Diretório raiz onde as imagens estão
diretorio_raiz = "."

# Encontra todas as imagens
imagens = encontrar_imagens(diretorio_raiz)
print(imagens)
exit()
# Junta as imagens em um grid
imagem_final = juntar_imagens(imagens, 100)

# Salva a imagem final
imagem_final.save("imagem_junta.jpg")
