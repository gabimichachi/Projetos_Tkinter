import tkinter as tk
from tkinter import ttk

class FlashcardC():
    def __init__(self):
        # criando a janela
        self.janela = tk.Tk()  # Corrigido para usar tk.Tk()
        self.janela.title("Flashcards")
        self.janela.geometry("700x500")
        self.janela.resizable(False, False)

        self.janela.iconbitmap("07_projeto_ Flashcards/main.ico")

        self.rotulo = ttk.Label(self.janela,
                        text="Gerenciar cartões de estudo",
                        background="lightskyblue",
                        foreground="black",
                        font=("impact", 20))
        self.rotulo.pack(pady=30)

        #Core CRUD:
        # Gerenciar 'cartões' (disciplina, pergunta [`tk.Text`], resposta [`tk.Text`]).

        # Desafio Extra:
        # Implementar um 'Modo Estudo'. Numa nova janela (`Toplevel`), o sistema mostra a *pergunta* de um cartão aleatório. O usuário clica num botão 'Revelar Resposta' para ver a resposta. 

        treeview = ttk.Treeview(self.janela)
        treeview.pack() 

        treeview.heading("#0", text="Coluna Chata")

        # defininido as colunas
        treeview["columns"] = ("disciplina", "pergunta", "resposta")
        treeview["show"] = "headings" # ocultando a coluna padrão    

        treeview.heading("disciplina", text="Nome Completo")
        treeview.heading("pergunta", text="Idade")
        treeview.heading("resposta", text="Cidade")

        # definindo o tamanho das colunas
        treeview.column("disciplina",anchor = "center")
        treeview.column("pergunta", anchor = "center")
        treeview.column("resposta", anchor = "center")
   




    def run(self):
        self.janela.mainloop()

if __name__ == "__main__":
    app = FlashcardC()
    app.run()
