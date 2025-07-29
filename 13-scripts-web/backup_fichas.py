import os
import shutil
from datetime import datetime

origem = 'fichas_pets'
destino_base = 'backup_fichas'

if not os.path.exists(origem):
    print(f"A pasta '{origem}' não foi encontrada. Verifique o caminho.")
    exit()

data_hoje = datetime.now().strftime('%Y-%m-%d')
destino = os.path.join(destino_base, data_hoje)
os.makedirs(destino, exist_ok=True)

total = 0
for arquivo in os.listdir(origem):
    caminho_origem = os.path.join(origem, arquivo)
    caminho_destino = os.path.join(destino, arquivo)

    if os.path.isfile(caminho_origem):
        shutil.copy2(caminho_origem, caminho_destino)
        total += 1
        print(f"Copiado: {arquivo}")

print(f"\nBackup concluído com sucesso. Total de fichas copiadas: {total}")
print(f"Backup salvo em: {destino}")