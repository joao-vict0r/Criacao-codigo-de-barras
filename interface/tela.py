import os
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from gerador_barras import criar_codigo_barras
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import win32print
import win32api

def gerar_codigo_barras():
    # Pasta local onde o código de barras será salvo
    destino_pasta = r"C:/Users/Joaov/Ambiente de Trabalho/Python projets/auto_boots/gerador_codigo_de_barras/imagem_etiqueta"
    
    try:
        # Gera o código de barras e salva a imagem
        caminho_imagem, codigo = criar_codigo_barras(destino=destino_pasta)
        exibir_imagem(caminho_imagem)
        label_codigo.config(text=f"Código gerado: {codigo}")

        messagebox.showinfo("Sucesso", f"Código de barras gerado e salvo em:\n{caminho_imagem}")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao gerar código de barras:\n{str(e)}")

def exibir_imagem(caminho_imagem):
    """Exibe a imagem do código de barras na interface."""
    img = Image.open(caminho_imagem)
    img = img.resize((300, 150), Image.Resampling.LANCZOS)
    img_tk = ImageTk.PhotoImage(img)
    canvas_imagem.create_image(0, 0, anchor=tk.NW, image=img_tk)
    canvas_imagem.image = img_tk

def imprimir_codigo_barras():
    """Imprime a imagem do código de barras ou salva em PDF se não encontrar impressora."""
    try:
        caminho_imagem = canvas_imagem.image.cget("file")
        printer_name = win32print.GetDefaultPrinter()
        if printer_name:
            win32api.ShellExecute(0, "print", caminho_imagem, f'/d:"{printer_name}"', ".", 0)
        else:
            raise Exception("Nenhuma impressora padrão encontrada")
    except Exception as e:
        salvar_em_pdf(caminho_imagem)
        messagebox.showerror("Erro", f"Erro ao imprimir código de barras. Salvo como PDF:\n{str(e)}")

def salvar_em_pdf(caminho_imagem):
    """Salva a imagem do código de barras em um arquivo PDF."""
    try:
        pdf_path = caminho_imagem.replace(".png", ".pdf")
        c = canvas.Canvas(pdf_path, pagesize=letter)
        c.drawImage(caminho_imagem, 100, 500, width=300, height=150)
        c.save()
        messagebox.showinfo("Sucesso", f"Código de barras salvo como PDF em:\n{pdf_path}")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao salvar código de barras como PDF:\n{str(e)}")

# Criação da interface principal
janela = tk.Tk()
janela.title("Gerador de Código de Barras")

frame_botao = tk.Frame(janela)
frame_botao.pack(pady=10, anchor=tk.CENTER)

canvas_imagem = tk.Canvas(janela, width=300, height=150)
canvas_imagem.pack(pady=10)

# Label para exibir o código gerado
label_codigo = tk.Label(janela, text="Código gerado: ")
label_codigo.pack(pady=10)

# Botão para gerar o código de barras
botao_gerar = tk.Button(frame_botao, text="Gerar Código de Barras", command=gerar_codigo_barras)
botao_gerar.pack(side=tk.LEFT, padx=5)

# Botão para imprimir o código de barras
botao_imprimir = tk.Button(frame_botao, text="Imprimir Código de Barras", command=imprimir_codigo_barras)
botao_imprimir.pack(side=tk.LEFT, padx=5)

janela.mainloop()