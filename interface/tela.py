import os
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from gerador_barras import criar_codigo_barras

def gerar_codigo_barras():
    destino_pasta = r"C:/Users/Joaov/Ambiente de Trabalho/Python projets/auto_boots/gerador_codigo_de_barras/imagem_etiqueta"
    
    try:
        # Chama a função para gerar o código de barras
        caminho_imagem, codigo = criar_codigo_barras(destino=destino_pasta)
        exibir_imagem(caminho_imagem)
        label_codigo.config(text=f"Código gerado: {codigo}")
        messagebox.showinfo("Sucesso", f"Código de barras gerado e salvo em:\n{caminho_imagem}")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao gerar código de barras:\n{str(e)}")

def exibir_imagem(caminho_imagem):
    """Exibe a imagem do código de barras na interface."""
    img = Image.open(caminho_imagem)
    img = img.resize((300, 150), Image.Resampling.LANCZOS)  # Substitui ANTIALIAS por Resampling.LANCZOS
    img_tk = ImageTk.PhotoImage(img)
    canvas_imagem.create_image(0, 0, anchor=tk.NW, image=img_tk)
    canvas_imagem.image = img_tk

# Criação da interface principal
janela = tk.Tk()
janela.title("Gerador de Código de Barras")

frame_destino = tk.Frame(janela)
frame_destino.pack(pady=10)

canvas_imagem = tk.Canvas(janela, width=300, height=150)
canvas_imagem.pack(pady=10)

# Label para exibir o código gerado
label_codigo = tk.Label(janela, text="Código gerado: ")
label_codigo.pack(pady=10)

# Botão para gerar o código de barras
botao_gerar = tk.Button(janela, text="Gerar Código de Barras", command=gerar_codigo_barras)
botao_gerar.pack(pady=10)
janela.mainloop()