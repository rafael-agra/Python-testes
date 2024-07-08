import os
import send2trash

def mover_arquivos_json_para_lixeira(pasta):
    for arquivo in os.listdir(pasta):
        if arquivo.endswith(".json"):
            caminho_arquivo = os.path.join(pasta, arquivo)
            send2trash.send2trash(caminho_arquivo)

# Exemplo de uso:
pasta_desejada = r"C:\Users\rafae\OneDrive\Pictures\2022\Photos from 2022"  # Substitua pelo caminho da pasta desejada
mover_arquivos_json_para_lixeira(pasta_desejada)
