import ttkbootstrap as ttk
from tkinter import Listbox
from tkinter import END
from tkinter import messagebox
import sqlite3


class Cadastro:
    def __init__(self, PaidoCadastro):
        self.Tarefas = ttk.Toplevel(PaidoCadastro)
                                  
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
                      text="Digite seu nome completo: ",
                      foreground="black",
                      font=("Times New Roman", 14))
        self.usuario.pack(pady=10)

        # ----------------------------------------------------
        self.add_usario = ttk.Entry(self.Tarefas, 
                                     style="secondary")

        self.add_usario.pack(padx=20, pady=30)
        # ----------------------------------------------------
        self.senha = ttk.Label(self.Tarefas,
                      text="Digite seu usuário: ",
                      foreground="black",
                      font=("Times New Roman", 14))
        self.senha.pack(pady=10)

        self.add_senha = ttk.Entry(self.Tarefas, 
                                     style="secondary")

        self.add_senha.pack(padx=20, pady=30)
        # ----------------------------------------------------
        self.confirmar = ttk.Label(self.Tarefas,
                      text="Digite a sua senha: ",
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
        

        botao_marcar = ttk.Button(frame_botao, 
                                  text="Cadastrar", 
                                  style="primary", 
                                  width=20,
                                  command=self.inserir_usuario)
        botao_marcar.pack(side="right",padx=10) 

        self.criar_tabela_usuario()

    def criar_tabela_usuario(self):
        # conectando o banco de dados
        conexao = sqlite3.connect("./bd_lista_tarefas.sqlite")

        # criar cursor 
        cursor = conexao.cursor()


        # executar o comando
        cursor.execute("""
                CREATE TABLE  IF NOT EXISTS usuario (
                            nome VARCHAR(80),
                            usuario VARCHAR (20) PRIMARY KEY,
                            senha VARCHAR (20)

            );
                    """)  
        # comito a transação
        conexao.commit()

        # encerro a conexão
        conexao.close()

    def inserir_usuario(self):
        # try:
            #   criar conexao
            conexao = sqlite3.connect("./bd_lista_tarefas.sqlite")

            # criar cursor
            cursor = conexao.cursor()

            nome = self.add_usario.get()
            usuario = self.add_senha.get()
            senha = self.add_confirmar.get()

    
            # executar
            cursor.execute("""
                            INSERT INTO usuario
                            (nome,
                            usuario,
                            senha)
                            VALUES
                            (?,
                            ?,
                            ?);
                            """,
                            [nome,
                            usuario,
                            senha]
                            )

            # comitar
            conexao.commit()

            # fechar conexão
            conexao.close()

            messagebox.showinfo("Sucesso!", "Usuário cadastrado com sucesso!")
        
        # except:
        #      messagebox.showerror("Erro!", "Erro ao cadastrar usuário. Tente novamente.")
             
        # finally:
        #      conexao.close()
    



    def run(self):
            self.Tarefas.mainloop()

if __name__ == "__main__":
        app = Cadastro()
        app.run()