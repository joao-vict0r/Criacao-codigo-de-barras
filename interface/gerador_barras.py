import random
import barcode
from barcode.writer import ImageWriter
import os
from datetime import datetime

def criar_codigo_barras(destino='codigo_barras'):
    # Obtém a data atual para nomear a subpasta
    data_atual = datetime.now().strftime("%Y-%m-%d")
    subpasta = os.path.join(destino, data_atual)

    # Cria a subpasta, caso não exista
    os.makedirs(subpasta, exist_ok=True)

    # Gera um código aleatório de 12 dígitos
    codigo = ''.join(random.choices('0123456789', k=12))  # 12 dígitos numéricos aleatórios
    barcode_file = os.path.join(subpasta, f"{codigo}.png")  # Caminho completo para o arquivo

    
    code = barcode.get('code128', codigo, writer=ImageWriter())
    barcode_file = code.save(barcode_file)  # Salva o arquivo no destino completo

    # Exibe o código gerado e o arquivo de saída
    print(f"Código de barras gerado: {codigo}")
    print(f"Arquivo salvo como: {barcode_file}")

    # Retorna o caminho do arquivo gerado e o código
    return barcode_file, codigo
