import os
import shutil

pasta = "arquivos"

tipos = {
    "Imagens": [".jpg", ".png", ".jpeg"],
    "Videos": [".mp4", ".avi"],
    "Musicas": [".mp3"],
    "Documentos": [".pdf", ".txt"]
}

for arquivo in os.listdir(pasta):
    caminho = os.path.join(pasta, arquivo)

    if os.path.isfile(caminho):
        for pasta_tipo, extensoes in tipos.items():
            if arquivo.lower().endswith(tuple(extensoes)):
                destino = os.path.join(pasta, pasta_tipo)
                os.makedirs(destino, exist_ok=True)
                shutil.move(caminho, destino)
