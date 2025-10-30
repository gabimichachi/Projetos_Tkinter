import ttkbootstrap as ttk

# criando a janela
janela = ttk.Window(themename="minty")
janela.geometry("800x600")

# criando o TreeView
treeview = ttk.Treeview(janela)
treeview.pack()

# defininido as colunas
treeview["columns"] = ("nome", "idade", "cidade")
treeview["show"] = "headings" # ocultando a coluna padrão

# definindo o cabeçalho
treeview.heading("#0", text="Coluna Chata")

# definindo as outras colunas
treeview.heading("nome", text="Nome Completo")
treeview.heading("idade", text="Idade")
treeview.heading("cidade", text="Cidade")

# definindo o tamanho das colunas
treeview.column("idade", width=80, anchor = "center")
treeview.column("nome", anchor = "center")
treeview.column("cidade", anchor = "center")

# inserindo dados
treeview.insert("", "end", values= ["Olivia", "16", "São Paulo"])

janela.mainloop()