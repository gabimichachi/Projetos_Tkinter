import ttkbootstrap as ttk
import tkinter.messagebox
from tkinter import messagebox

class calculadoraIMC():
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
                        text="Calculo de IMC",
                        background="mediumpurple",
                        foreground="black",
                        font=("Impact", 20))
        self.rotulo.pack(pady=30)

        #perguntar peso
        self.resposta = ttk.Label(self.janela,
                      text="Digite seu Peso: ",
                      foreground="white",
                      font=("Times New Roman", 14))
        self.resposta.pack(pady=10)


        #digitar peso
        self.peso = ttk.Entry(self.janela,
                            text="",
                                background="pink",
                                foreground="white",
                                font=("Arial", 12),
                                style="primary")

        self.peso.pack(pady=2)

        #perguntar altura
        self.resposta = ttk.Label(self.janela,
                      text="Digite sua Altura: ",
                      foreground="white",
                      font=("Times New Roman", 14))
        self.resposta.pack(pady=10)

        #digitar altura
        self.altura = ttk.Entry(self.janela,
                            text="",
                                background="pink",
                                foreground="white",
                                font=("Arial", 12),
                                style="primary")

        self.altura.pack(pady=2)

        #criar botao
        self.button_botao= ttk.Button(self.janela,
                                text="Calcular",
                                style="primary",
                                command=self.calcular_imc
                                )
        self.button_botao.pack(pady=20)

        #perguntar peso
        self.resultado_label = ttk.Label(self.janela,
                      text="valor do IMC: ",
                      foreground="white",
                      font=("Georgia", 14))
        self.resultado_label.pack(pady=10)

        #classificaçao
        self.classificacao_label = ttk.Label(self.janela,
                      text="",
                      foreground="white",
                      font=("Times New Roman", 14))
        self.classificacao_label.pack(pady=10)


    def calcular_imc(self):

        try:
            peso_texto = float (self.peso.get())
            altura_texto = float (self.altura.get())
            #calcula o indice de massa corporal (IMC)
            altura_metros = altura_texto / 100
            self.resultado_imc = peso_texto / (altura_metros ** 2)
            self.resultado_label.config(text=f"valor do IMC: {self.resultado_imc:.2f}")

        except ValueError:
            tkinter.messagebox.showerror(title="ERRO", message="Valores incorretos")
            

        

        
        #classificaçao
        self.classificacao_colocar()
        self.classificacao_label.config(text=self.classificacao)

    def classificacao_colocar(self):

        if self.resultado_imc < 18.5:
            self.classificacao = "Abaixo do Peso Normal"

        if self.resultado_imc >= 18.5 and self.resultado_imc <= 24.9:
            self.classificacao = "No Peso Normal"

        if self.resultado_imc >= 25.0 and self.resultado_imc <= 29.9:
            self.classificacao = "Em Excesso de peso"

        if self.resultado_imc >= 30.0 and self.resultado_imc <= 34.9:
            self.classificacao = "Com Obesidade Grau 1!"

        if self.resultado_imc >= 35.0 and self.resultado_imc <= 39.9:
            self.classificacao = "Com Obesidade Grau 2!"

        if self.resultado_imc >= 40.0:
            self.classificacao = "Com Obesidade Grau 3!"
        
        return self.classificacao


        #clicar no botao
        def ao_clicar_botao():
            texto = self.resposta.get()
            self.rotulo.config(text=texto)

        #resultado
        self.label_resultado = ttk.Label(self.janela,
                                    text="",
                                    foreground="white",
                                    font=("Arial", 20))

        self.label_resultado.pack(pady=20)

        


    def run(self):
        self.janela.mainloop()

if __name__ == "__main__":
    chat = calculadoraIMC()
    chat.run()