import ttkbootstrap as ttk
from classe_bot_gemini import Gemini_Bot

class Janela_chat():
    def __init__(self):
        # criando a janela
        self.janela = ttk.Window(themename= "vapor",
                                title="Dr. Sleep")
        self.janela.geometry("800x600")
        
        #impede que o usuario redimensione a janela
        self.janela.resizable(False, False)

        #mudando a cor de fundo da janela
        self.janela.iconbitmap("03_01_boot_gemini.py/painel-ravena.ico")

        # criando um rótulo
        self.rotulo = ttk.Label(self.janela,
                        text="💤Dr. Sleep💤",
                        background="mediumpurple",
                        foreground="black",
                        font=("Impact", 25))
        self.rotulo.pack(pady=20)
        
        #faça sua pergunta
        self.resposta = ttk.Label(self.janela,
                      text="Digite sua pergunta sobre sono:",
                      foreground="white",
                      font=("Comic Sans MS", 15))
        self.resposta.pack(pady=10)

        #digitar texto
        self.entry_resposta = ttk.Entry(self.janela,
                            text="",
                                background="pink",
                                foreground="white",
                                font=("Arial", 12),
                                style="primary")


        self.entry_resposta.pack(pady=10)

        #clicar no botao
        def ao_clicar_botao():
          texto = self.resposta.get()
          self.rotulo.config(text=texto)

        #criar botao
        self.button_sono= ttk.Button(self.janela,
                        text="perguntar",
                        command=self.responder,
                        style="secondary"
                        )
        self.button_sono.pack(pady=10)

        #criar segundo botao
        self.button_sono= ttk.Button(self.janela,
                        text="perguntar",
                        command=self.responder,
                        style="primary"
                        )
        self.button_sono.pack(pady=10)

        #resultado
        self.label_resultado = ttk.Label(self.janela,
                                    text="",
                                    foreground="white",
                                    font=("Arial", 20))

        self.label_resultado.pack(pady=20)

        self.st = ttk.ScrolledText(self.janela, height=10, wrap="word")
        self.st.pack(pady=10, padx=10, fill="both", expand=True)

        # criando o objeto robo (instancando a classe) 
        self.robo = Gemini_Bot()

        #funcao do botao
    def responder(self):
        """esta funcao pega a pergunta sobre sono e responde"""
        pergunta = self.entry_resposta.get()
        resposta = self.robo.enviar_mensagem(pergunta)
        self.label_resultado.config(text=resposta)

        self.st.delete("1.0", ttk.END)
        self.st.insert("1.0", resposta)
        
    def run(self):
        self.janela.mainloop()

if __name__ == "__main__":
    chat = Janela_chat()
    chat.run()
    
