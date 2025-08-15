import tkinter as tk

#criando uma janela
janela = tk.Tk()
janela.title("Hello World")

# criando um rótulo
rotulo = tk.Label(janela,
                  text="Olá, Mundo!",
                   font=("Arial", 24),
                   bg="pink",
                   fg="black")

rotulo.pack(pady=20)

#digite seu nome
nome = tk.Label(janela,
                text="Digite seu nome:",
                font=("Arial", 14),
                bg="pink",
                fg="black")

nome.pack(pady=10)

#digitar texto
entrada = tk.Entry(janela,
                    text="Digite seu nome:",
                      font=("Arial", 18),
                        bg="pink",
                        fg="white")

entrada.pack(pady=10)

#clicar no botao
def ao_clicar_botao():
    texto = entrada.get()
    rotulo.config(text=texto)


#criar botao
button_bomdia= tk.Button(janela,
                   text="Desejar Bom Dia",
                   font=("Arial", 18),
                   bg="pink",
                   fg="black",
                   command=ao_clicar_botao)

button_bomdia.pack(pady=10)

#mudando a cor de fundo da janela
janela.config(bg="lightblue")
janela.iconbitmap("01_Hello_World/images.ico")
janela.geometry("800x400+200+300")

#impede que o usuario redimensione a janela
janela.resizable(False, False)

#loop para manter a janela aberta
janela.mainloop()

