# import sqlite3

# # Nome do arquivo do banco de dados SQLite
# DATABASE_NAME = "flashcards.db"

# def conectar_db():
#     """Cria e retorna a conexão com o banco de dados."""
#     # A conexão será criada se o arquivo não existir
#     conn = sqlite3.connect(DATABASE_NAME)
#     return conn

# def inicializar_db():
#     """Inicializa a tabela de flashcards se ela não existir."""
#     conn = None
#     try:
#         conn = conectar_db()
#         cursor = conn.cursor()
#         # Cria a tabela 'flashcards' com um ID autoincrementável
#         cursor.execute("""
#             CREATE TABLE IF NOT EXISTS flashcards (
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 disciplina TEXT NOT NULL,
#                 pergunta TEXT NOT NULL,
#                 resposta TEXT NOT NULL
#             )
#         """)
#         conn.commit()
#     except sqlite3.Error as e:
#         print(f"Erro ao inicializar o banco de dados: {e}")
#     finally:
#         if conn:
#             conn.close()

# def salvar_flashcard(disciplina, pergunta, resposta):
#     """Salva um novo flashcard no banco de dados e retorna o ID gerado."""
#     conn = None
#     try:
#         conn = conectar_db()
#         cursor = conn.cursor()
#         cursor.execute("""
#             INSERT INTO flashcards (disciplina, pergunta, resposta)
#             VALUES (?, ?, ?)
#         """, (disciplina, pergunta, resposta))
#         conn.commit()
#         # Retorna o ID da linha recém-inserida
#         return cursor.lastrowid
#     except sqlite3.Error as e:
#         print(f"Erro ao salvar flashcard: {e}")
#         return None
#     finally:
#         if conn:
#             conn.close()

# def carregar_flashcards():
#     """Carrega todos os flashcards do banco de dados."""
#     conn = None
#     try:
#         conn = conectar_db()
#         cursor = conn.cursor()
#         # Seleciona todos os campos, incluindo o ID (importante para o Treeview ou exclusão)
#         cursor.execute("SELECT id, disciplina, pergunta, resposta FROM flashcards ORDER BY disciplina, id")
#         cartoes = cursor.fetchall()
#         return cartoes
#     except sqlite3.Error as e:
#         print(f"Erro ao carregar flashcards: {e}")
#         return []
#     finally:
#         if conn:
#             conn.close()

# # Garante que o banco de dados seja inicializado na primeira vez que o módulo for importado
# inicializar_db()