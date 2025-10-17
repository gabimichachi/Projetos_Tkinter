import tkinter
import ttkbootstrap as ttk
import tkinter.messagebox
from classe_lista_tarefas import Tarefas

class Login():
    def __init__(self,janela_pai):
        self.janela_pai = janela_pai
# criando a janela
        self.janela = ttk.Toplevel(janela_pai)(themename= "minty",
                                title="campo de login")
        self.janela.geometry("800x600")

        # confiurando para que quandpo feche a kanela de login ele encerre o prohgrama
        self.janela.protocol("WM_DELETE_WINDOW", self.fechar)

#impede que o usuario redimensione a janela
        self.janela.resizable(False, False)

#mudando a cor de fundo da janela
        self.janela.iconbitmap("05_lista_de_tarefas/cadeado.ico")

#criando um rótulo
        self.rotulo = ttk.Label(self.janela,
                        text="Login",
                        background="pink",
                        foreground="black",
                        font=("Impact", 20))
        self.rotulo.pack(pady=30)

#perguntar USUARIO
        self.usuario = ttk.Label(self.janela,
                      text="USUÁRIO: ",
                      foreground="black",
                      font=("Comic Sans MS", 12))
        self.usuario.pack(pady=10)

#digitar usuario
        self.digitar = ttk.Entry(self.janela,
                            text="",
                                background="pink",
                                foreground="pink",
                                font=("Arial", 12),
                                style="secondary")

        self.digitar.pack(pady=2)

#perguntar SENHA
        self.senha = ttk.Label(self.janela,
                      text="SENHA: ",
                      foreground="black",
                      font=("Comic Sans MS", 12))
        self.senha.pack(pady=10)

#digitar SENHA
        self.digite = ttk.Entry(self.janela,
                            text="",
                            show="•",
                                background="pink",
                                foreground="pink",
                                font=("Arial", 12),
                                style="secondary")

        self.digite.pack(pady=2)

        self.frame_botao = ttk.Frame()
        self.frame_botao.pack()

 #criar botao
        self.button_botao= ttk.Button(self.frame_botao,
                                text="logar",
                                style="secondary",
                                padding= (20,10),
                                command=self.logar
                                )
        self.button_botao.pack(side="left", padx=10, pady=20)

        #criar botao
        self.button_botao= ttk.Button(self.frame_botao,
                                text="sair",
                                padding= (20,10),
                                style="secondary",
                                command=self.fechar
                                )
        self.button_botao.pack(side="right", padx=10, pady=20)

    # def tarefas(self):
    #     self.janela.destroy()
    #     import lista_tarefas
    #     app = lista_tarefas.Tarefas()
        # app.run()

    def logar(self):
        usuario_senha = (self.digitar.get())
        usuario_digitar = (self.digite.get())

        if usuario_senha == "oliviawyy" and usuario_digitar == "1234":
                self.janela.destroy()
                # reexibe a janela principal (janela de tarefas)
                self.janela_pai.deiconify()
                # janela_tarefas = Tarefas()
                # janela_tarefas.run()
                
        else:
            tkinter.messagebox.showerror(title= "Erro no login", message = "Usuário ou senha incorretos!")

    def fechar(self):
        resposta = tkinter.messagebox.askyesno(title="fechar", message="voce tem certeza que deseja sair?")
        if resposta == True:
                self.janela.destroy()


    def run(self):
        self.janela.mainloop()

if __name__ == "__main__":
    app = Login()
    app.run()
