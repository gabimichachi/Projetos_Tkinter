import ttkbootstrap as ttk


class Tarefas():
    def __init__(self):
        self.janela = ttk.Window(themename= "minty",
                                title="lista de tarefas")
        self.janela.geometry("800x600")

#impede que o usuario redimensione a janela
        self.janela.resizable(False, False)

#mudando a cor de fundo da janela
        self.janela.iconbitmap("05_lista_de_tarefas/ico.ico")
       
#titulo
        self.titulo = ttk.Label(self.janela,
                        text="Lista de Tarefas ─.✦",
                        background="pink",
                        foreground="black",
                        font=("Impact", 20))
        self.titulo.pack(pady=30)






    def run(self):
        self.janela.mainloop()

if __name__ == "__main__":
    app = Tarefas()
    app.run()
