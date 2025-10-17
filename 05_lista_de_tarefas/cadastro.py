import ttkbootstrap as ttk
from tkinter import Listbox
from tkinter import END
from tkinter import messagebox


class Cadastro:
    def __init__(self, janela_pai):
        self.Tarefas = ttk.Toplevel(janela_pai)(themename="minty",
                                  title="lista de cadastro")
        self.Tarefas.geometry("800x600")

    #impede que o usuario redimensione a janela
        self.Tarefas.resizable(False, False)

    #mudando a cor de fundo da janela
        self.Tarefas.iconbitmap("05_lista_de_tarefas/cadastro.png")
       
       #titulo
        self.titulo = ttk.Label(self.Tarefas,
                         text="Lista de Cadastro ─.✦",
                         background="pink",
                         foreground="black",
                         style="secondary",
                         font=("Impact", 20))
        
        self.titulo.pack(pady=30)
        frame_add = ttk.Frame(self.Tarefas)
        frame_add.pack(padx=200, fill="x")


        self.usuario = ttk.Label(self.Tarefas,
                      text="Digite seu Usuário: ",
                      foreground="black",
                      font=("Times New Roman", 14))
        self.usuario.pack(pady=10)

        # ----------------------------------------------------
        self.add_usario = ttk.Entry(self.Tarefas, 
                                     style="secondary")

        self.add_usario.pack(padx=20, pady=30)
        # ----------------------------------------------------
        self.senha = ttk.Label(self.Tarefas,
                      text="Digite seu Peso: ",
                      foreground="black",
                      font=("Times New Roman", 14))
        self.senha.pack(pady=10)

        self.add_senha = ttk.Entry(self.Tarefas, 
                                     style="secondary")

        self.add_senha.pack(padx=20, pady=30)
        # ----------------------------------------------------
        self.confirmar = ttk.Label(self.Tarefas,
                      text="Digite seu Peso: ",
                      foreground="black",
                      font=("Times New Roman", 14))
        self.confirmar.pack(pady=10)

        self.add_confirmar = ttk.Entry(self.Tarefas, 
                                     style="secondary")

        self.add_confirmar.pack(padx=20, pady=30)
        # ----------------------------------------------------

        frame_botao = ttk.Frame(self.Tarefas)
        frame_botao.pack(side="bottom", 
                         expand=True)
        
        botao_excluir = ttk.Button(frame_botao,
                                   command=self,
                                   text="Excluir", 
                                   style="danger", 
                                   width=20) 
        botao_excluir.pack(side="left",padx=10)

        botao_marcar = ttk.Button(frame_botao, 
                                  text="Marcar como concluido", 
                                  style="primary", 
                                  width=20,
                                  command=self)
        botao_marcar.pack(side="right",padx=10)
    



    def run(self):
            self.Tarefas.mainloop()

if __name__ == "__main__":
        app = Cadastro()
        app.run()