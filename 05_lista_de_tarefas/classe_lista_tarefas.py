import ttkbootstrap as ttk
from tkinter import Listbox
from tkinter import END
from tkinter import messagebox
import sqlite3


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
                   style="secondary",
                   command=self.adicionar_tarefa).pack(side="right")

        self.lista = Listbox(self.janela, 
                        font=("Segoe UI", 12),
                        width=80)
        self.lista.pack(pady=30)
        
        frame_botao = ttk.Frame(self.janela)
        frame_botao.pack(side="bottom", 
                         expand=True)

        botao_excluir = ttk.Button(frame_botao,
                                   command=self.excluir_tarefa ,
                                   text="Excluir", 
                                   style="danger", 
                                   width=20) 
        botao_excluir.pack(side="left",padx=10)

        botao_marcar = ttk.Button(frame_botao, 
                                  text="Marcar como concluido", 
                                  style="primary", 
                                  width=20,
                                  command=self.marcar_concluido)
        botao_marcar.pack(side="right",padx=10)



    def adicionar_tarefa(self):
        #pegando o texto da caixa de texto 
        tarefa = self.add_tarefa.get()

        #inserindo a tarefa na list
        self.lista.insert(END, tarefa)
        self.add_tarefa.delete(0, END)  # Limpa o campo de entrada após adicionar


        # tarefa.pack()

    def excluir_tarefa(self):
        # Obtém o índice da tarefa selecionada
        excluir_indice = self.lista.curselection()

        if excluir_indice:
            self.lista.delete(excluir_indice)
        else:
            messagebox.showerror(message="Selecione um item antes de excluir!")

        # self.lista.delete(excluir_indice[0])  # Exclui a tarefa selecionada

    def marcar_concluido(self):
        tarefa_selecionada = self.lista.curselection()
        texto = self.lista.get(tarefa_selecionada)

        if tarefa_selecionada:
            self.lista.delete(tarefa_selecionada[0])
            self.lista.insert(tarefa_selecionada[0], texto + "   concluído☀︎")
            self.lista.itemconfig(tarefa_selecionada, {"fg": "green", "selectforeground": "green"})
            
        else:
            messagebox.showerror("Aviso", "Selecione uma tarefa para concluir.")



# (pady=20, padx=20, fill='both'adfegrgrhtehe)





    def run(self):
        self.janela.mainloop()

if __name__ == "__main__":
    app = Tarefas()
    app.run()
