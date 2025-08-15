import tkinter as tk

#criando uma janela
janela = tk.Tk()
janela.title("Hello World")

# criando um rótulo
rotulo = tk.Label(janela, text="Olá, Mundo!")
rotulo.pack()

#loop para manter a janela aberta
janela.mainloop()

#mudando a cor de fundo da janela
janela.config(bg="lightblue")


