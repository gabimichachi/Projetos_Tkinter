import google.generativeai as genai

class Gemini_Bot:
    """Classe responsável por gerenciar o modelo do Gemini."""
    
    def __init__(self):
        genai.configure(api_key="AIzaSyAwxjTXssSQ9gLXB-Q9QlATJYTk78bpE0g")
        
        instrucao_sistema = """
            Você é especialista em dormir, com 20 anos de experiência.
            Seu nome é Dr. Sleep. Você deve responder a todas as perguntas de forma 
            profissional, detalhada e focada exclusivamente no mundo do sono. 
            Se o usuário perguntar sobre outro assunto, gentilmente redirecione a conversa 
            de volta para o sono, afirmando que seu conhecimento é especializado.
            """
        
        self.model = genai.GenerativeModel(
            model_name='gemini-1.5-flash',
            system_instruction=instrucao_sistema
        )
        self.chat = self.model.start_chat()

    def enviar_mensagem(self, mensagem: str) -> str:
        """Envia mensagem para o modelo e retorna a resposta."""
        response = self.chat.send_message(mensagem)
        return response.text
    















