import ttkbootstrap as ttk
from tkinter import Listbox
from tkinter import END
from tkinter import messagebox
import sqlite3
from login import Login


class Tarefas():
    def __init__(self, usuario_logado=None):

        # usuario que esta logado
        self.usuario_logado = usuario_logado

        print(usuario_logado)
        # criando a janela
        self.janela = ttk.Window( themename="minty")

        # criando o titulo
        self.janela.title("Lista de Tarefas")

        # tamanho da janela
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

        conexao = sqlite3.connect("./bd_lista_tarefas.sqlite")

        #Criando responsavel por comandar o Banco de Dados 
        cursor = conexao.cursor()

        #Criando tabela 
        sql_para_criar_tabela = """
                                CREATE TABLE IF NOT EXISTS tarefa (
                                codigo integer primary key autoincrement,
                                descricao_tarefa varchar(200),
                                usuario varchar(20)
                                );
                                """
        cursor.execute(sql_para_criar_tabela)

        # Confirma as alterações
        conexao.commit()
        
        #fechei a conexão
        cursor.close()
        conexao.close()

        #abrino=do a janela de login
        Login(self)
        
        #escondendo  ajanela da lista tarefas
        self.janela.withdraw()

        self.atualizar_lista()

        # lista_tarefas = Logar(self.janela)

    def atualizar_lista(self):

        #atualizar tarefa 

        conexao = sqlite3.connect("./bd_lista_tarefas.sqlite")
        cursor = conexao.cursor()

        sql_para_selecionar_tarefas = """
                                        select codigo, descricao_tarefa from tarefa
                                        where usuario = ?;
                                        """
        cursor.execute(sql_para_selecionar_tarefas, [self.usuario_logado])

        lista_de_tarefas =cursor.fetchall()

        cursor.close()
        conexao.close()

        #inserindo items listbox
        for linha in lista_de_tarefas:
            self.lista.insert("end", linha[1])

    
    def adicionar_tarefa(self):
        #pegango o texto da caixa de texto
        tarefa = self.add_tarefa.get()

        self.lista.insert("end", tarefa)

        conexao = sqlite3.connect("./bd_lista_tarefas.sqlite")
        cursor = conexao.cursor()

        sql_insert = """
                        INSERT INTO tarefa (descricao_tarefa, usuario)
                        VALUES (?, ?)
                        
                    """
        valores = (tarefa, self.usuario_logado)
        cursor.execute(sql_insert, valores)

        conexao.commit()
        cursor.close()
        conexao.close()

        # tarefa.pack()

    def excluir_tarefa(self):
        excluir_indice = self.lista.curselection()

        if excluir_indice:
            texto_tarefa = self.lista.get(excluir_indice[0])  # Obter o texto da tarefa
            self.lista.delete(excluir_indice)

            conexao = sqlite3.connect("./bd_lista_tarefas.sqlite")
            cursor = conexao.cursor()

            sql_delete = """
                            DELETE FROM tarefa WHERE descricao_tarefa = ?;
                        """
            cursor.execute(sql_delete, (texto_tarefa,))  # Corrigido
            conexao.commit()

            cursor.close()
            conexao.close()
        else:
            messagebox.showerror(message="Selecione um item antes de excluir")

    def marcar_concluido(self):
        item_selecionada = self.lista.curselection()

        if item_selecionada:
            texto_tarefa = self.lista.get(item_selecionada[0])  # Corrigido

            if "   concluído☀︎" not in texto_tarefa:
                self.lista.delete(item_selecionada[0])
                texto_tarefa_concluido = texto_tarefa + "   concluído☀︎"
                self.lista.insert(item_selecionada[0], texto_tarefa_concluido)

                with sqlite3.connect("./bd_lista_tarefas.sqlite") as conexao:
                    cursor = conexao.cursor()

                    sql_update = """
                                UPDATE tarefa
                                SET descricao_tarefa = ?
                                WHERE descricao_tarefa = ?;
                                """
                    valores = (texto_tarefa_concluido, texto_tarefa)
                    cursor.execute(sql_update, valores)
        else:
            messagebox.showerror("Aviso", "Selecione uma tarefa para concluir.")

    def run(self):
        self.janela.mainloop()

if __name__ == "__main__":
    app = Tarefas()
    app.run()
