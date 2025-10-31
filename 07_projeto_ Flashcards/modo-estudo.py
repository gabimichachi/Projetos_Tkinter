import tkinter as tk
from flashcards import FlashcardC
from tkinter import Tk, Toplevel, messagebox
import random

class Estudo():
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("Modo Estudo")
        self.janela.geometry("800x700")
        self.janela.resizable(False, False)

        self.rotulo = tk.Label(self.janela,
                        text="Modo estudo 𓇼𓏲*ੈ✩‧₊˚🎐",
                        background="lightskyblue",
                        foreground="navy",
                        font=("Kristen ITC", 21))
        self.rotulo.pack(pady=30)


        # Corrigido: botão chama a função
        self.botao_estudo = tk.Button(self.janela, text="Iniciar Modo Estudo", command=self.abrir_modo_estudo)
        self.botao_estudo.pack(pady=20)

    def abrir_modo_estudo(self):
        if not FlashcardC.lista_flashcards:
            messagebox.showinfo("Aviso", "Nenhum card disponível para estudo.")
            return
        
        # Corrigido: nome da variável
        flashcard = random.choice(FlashcardC.lista_flashcards)
        top = Toplevel(self.janela)
        top.title("Modo Estudo")
        top.geometry("400x300")
        top.resizable(False, False)

        pergunta_label = tk.Label(top, text=f"Pergunta:\n{flashcard.pergunta}", font=("Arial", 14), wraplength=350)
        pergunta_label.pack(pady=30)

        def revelar_resposta():
            resposta_label.config(text=f"Resposta:\n{flashcard.resposta}")

        resposta_label = tk.Label(top, text="", font=("Arial", 14), wraplength=350)
        resposta_label.pack(pady=10)

        botao_revelar = tk.Button(top, 
                                  text="Revelar Resposta", 
                                  command=revelar_resposta)
        botao_revelar.pack(pady=20)

    def run(self):
        self.janela.mainloop()

if __name__ == "__main__":
    app = Estudo()
    app.run()
