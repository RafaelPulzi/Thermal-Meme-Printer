from escpos.printer import Win32Raw
from PIL import Image
import os
import random

# =============================
# CONFIG
# =============================

PRINTER_NAME = "POS-58"
IMAGES_FOLDER = "images"

# Largura em pixels da impressora térmica (58mm)
PRINTER_WIDTH_PX = 384 

# =============================
# PROCESSAR IMAGEM
# =============================

def preparar_imagem(caminho: str) -> Image.Image:
    if not os.path.exists(caminho):
        raise FileNotFoundError(f"Imagem não encontrada: {caminho}")

    img = Image.open(caminho)

    if img.mode != "RGB":
        img = img.convert("RGB")

    largura_original, altura_original = img.size
    proporcao = PRINTER_WIDTH_PX / largura_original
    nova_altura = int(altura_original * proporcao)

    # Redimensiona a imagem para caber na impressora
    img = img.resize((PRINTER_WIDTH_PX, nova_altura), Image.LANCZOS)

    # O python-escpos já faz a conversão para P&B, mas fazer manualmente 
    # com FloydSteinberg garante uma qualidade visual muito melhor.
    img = img.convert("L")
    img = img.convert("1", dither=Image.FLOYDSTEINBERG)

    return img

# =============================
# ESCOLHER IMAGEM ALEATÓRIA
# =============================

def escolher_imagem_aleatoria():
    if not os.path.exists(IMAGES_FOLDER):
        raise FileNotFoundError(f"Pasta não encontrada: {IMAGES_FOLDER}")

    arquivos = [
        f for f in os.listdir(IMAGES_FOLDER)
        if f.lower().endswith((".png", ".jpg", ".jpeg", ".bmp", ".gif"))
    ]

    if not arquivos:
        raise Exception("Nenhuma imagem encontrada na pasta images")

    escolhido = random.choice(arquivos)
    return os.path.join(IMAGES_FOLDER, escolhido)

# =============================
# IMPRIMIR
# =============================

def imprimir_imagem(caminho: str):
    print(f"Preparando imagem: {caminho}")
    img = preparar_imagem(caminho)

    print(f"Tamanho final: {img.size[0]}x{img.size[1]}px")
    print(f"Conectando à impressora: {PRINTER_NAME}")

    try:
        p = Win32Raw(PRINTER_NAME)
    except Exception as e:
        print(f"Erro ao conectar na impressora: {e}")
        return

    try:
        # A MÁGICA ACONTECE AQUI:
        # Mudamos o 'impl' para 'bitImageColumn' para garantir compatibilidade 
        # com impressoras POS-58 genéricas.
        p.image(img, impl="bitImageColumn", center=True)
        
        # Opcional: Avança um pouco o papel antes de cortar
        p.text("\n")
        
        # Algumas POS-58 não têm guilhotina automática, mas se a sua tiver, isso vai funcionar
        try:
            p.cut()
        except:
            pass # Ignora erro se não tiver guilhotina
            
        print("Impresso com sucesso!")
    except Exception as e:
        print(f"Erro ao imprimir: {e}")

# =============================
# MAIN
# =============================

if __name__ == "__main__":
    try:
        caminho = escolher_imagem_aleatoria()
        imprimir_imagem(caminho)
    except Exception as e:
        print(f"Erro: {e}")
