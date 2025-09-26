import ttkbootstrap as ttk
from tkinter import Listbox


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
                         style="secondary",
                         font=("Impact", 20))
        
        self.titulo.pack(pady=30)
        frame_add = ttk.Frame(self.janela)
        frame_add.pack(padx=200, fill="x")

        self.add_tarefa = ttk.Entry(frame_add, 
                                    style="secondary")

        self.add_tarefa.pack(side="left", 
                             fill="x", 
                             expand=True)


        ttk.Button(frame_add,
                   text="adicionar",
                   style="secondary").pack(side="right")

        lista = Listbox(self.janela, font=("Segoe UI", 12),width=80)
        lista.pack(pady=30)
        
        frame_botao = ttk.Frame(self.janela)
        frame_botao.pack(side="bottom", expand=True)

        botao_excluir = ttk.Button(frame_botao, text="Excluir", style="secondary", width=30)
        botao_excluir.pack(side="left",padx=10)

        botao_marcar = ttk.Button(frame_botao, text="Marcar como concluido", style="secondary", width=30)
        botao_marcar.pack(side="right",padx=10)

# (pady=20, padx=20, fill='both'adfegrgrhtehe)





    def run(self):
        self.janela.mainloop()

if __name__ == "__main__":
    app = Tarefas()
    app.run()
