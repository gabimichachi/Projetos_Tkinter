import ttkbootstrap as tk

class Janela_principal:
    """classe para a criacao da janela principal"""

    def __init__(self):
        
      #criando uma janela
      self.janela = tk.Window(themename="vapor")
      self.janela.title("Hello World")

      #mudando a cor de fundo da janela
      self.janela.config(background="lightblue")
      self.janela.iconbitmap("01_Hello_World/images.ico")
      self.janela.geometry("800x400+200+300")

      #impede que o usuario redimensione a janela
      self.janela.resizable(False, False)

      # criando um rótulo
      self.rotulo = tk.Label(self.janela,
                        text="Olá, Mundo!",
                        background="pink",
                        foreground="black",
                        font=("Arial", 12))

      self.rotulo.pack(pady=20)

      #digite seu nome
      self.nome = tk.Label(self.janela,
                      text="Digite seu nome:",
                      background="pink",
                      foreground="black",
                      font=("Arial", 12))

      self.nome.pack(pady=10)

      #digitar texto
      self.entrada = tk.Entry(self.janela,
                          text="Digite seu nome:",
                              background="pink",
                              foreground="white",
                              font=("Arial", 12))

      self.entrada.pack(pady=10)

      #clicar no botao
      def ao_clicar_botao():
          texto = self.entrada.get()
          self.rotulo.config(text=texto)


      #criar botao
      self.button_bomdia= tk.Button(self.janela,
                        text="Desejar Bom Dia",
                        command=self.desejar_bomdia,
                        font=("Arial", 20)
                        )

      self.button_bomdia.pack(pady=10)

      #resultado
      self.label_resultado = tk.Label(self.janela,
                                  text="",
                                  background="pink",
                                  foreground="black",
                                  font=("Arial", 30))

      self.label_resultado.pack(pady=20)

    def run(self):
        """inicia a janela"""
          
        #loop para manter a janela aberta
        self.janela.mainloop()

    #funcao do botao
    def desejar_bomdia(self):
        """esta funcao pega o nome digitado na caixa de texto e deseja um bom dia"""
        self.nome = self.entrada.get()
        self.label_resultado.config(text=f"Bom Dia, {self.nome}")

        #loop para manter a janela aberta
        self.janela.mainloop()
