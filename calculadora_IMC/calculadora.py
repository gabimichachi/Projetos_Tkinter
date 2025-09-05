import ttkbootstrap as ttk

class Janela_chat():
    def __init__(self):
        # criando a janela
        self.janela = ttk.Window(themename= "vapor",
                                title="Calculadora IMC")
        self.janela.geometry("800x600")

        #impede que o usuario redimensione a janela
        self.janela.resizable(False, False)

        #mudando a cor de fundo da janela
        self.janela.iconbitmap("calculadora_IMC/peso.ico")

        # criando um rótulo
        self.rotulo = ttk.Label(self.janela,
                        text="Coloque os seus dados na calculadora e calcule o seu IMC:",
                        background="mediumpurple",
                        foreground="black",
                        font=("Impact", 14))
        self.rotulo.pack(pady=30)

        #faça sua pergunta
        self.resposta = ttk.Label(self.janela,
                      text="Digite sua ",
                      foreground="white",
                      font=("Comic Sans MS", 15))
        self.resposta.pack(pady=10)









    def run(self):
        self.janela.mainloop()

if __name__ == "__main__":
    chat = Janela_chat()
    chat.run()