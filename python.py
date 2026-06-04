import tkinter as tk
from tkinter import filedialog, messagebox
import qrcode
from PIL import Image, ImageTk

def gerar_qrcode():
    texto = entrada.get()

    if not texto:
        messagebox.showwarning("Aviso", "Digite um texto ou URL.")
        return

    qr = qrcode.make(texto)
    qr.save("qrcode.png")

    img = Image.open("qrcode.png")
    img = img.resize((250, 250))

    foto = ImageTk.PhotoImage(img)

    painel.config(image=foto)
    painel.image = foto

def salvar():
    arquivo = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG", "*.png")]
    )

    if arquivo:
        qr = qrcode.make(entrada.get())
        qr.save(arquivo)

janela = tk.Tk()
janela.title("QR Generator")
janela.geometry("500x500")
janela.configure(bg="#f5f2eb")

titulo = tk.Label(
    janela,
    text="QR Code Generator",
    font=("Segoe UI", 18, "bold"),
    bg="#f5f2eb",
    fg="#3d2b1f"
)
titulo.pack(pady=20)

entrada = tk.Entry(
    janela,
    font=("Segoe UI", 12),
    width=40
)
entrada.pack(pady=10)

btn = tk.Button(
    janela,
    text="Gerar QR Code",
    font=("Segoe UI", 11),
    bg="#6b4f3b",
    fg="white",
    padx=20,
    pady=8,
    command=gerar_qrcode
)
btn.pack(pady=10)

painel = tk.Label(janela, bg="#f5f2eb")
painel.pack(pady=15)

btn_salvar = tk.Button(
    janela,
    text="Salvar PNG",
    font=("Segoe UI", 11),
    bg="#2e7d32",
    fg="white",
    padx=20,
    pady=8,
    command=salvar
)
btn_salvar.pack()

janela.mainloop()