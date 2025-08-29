from google import genai

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.cliente(api_key="AIzaSyAwxjTXssSQ9gLXB-Q9QlATJYTk78bpE0g")

response = client.models.generate_content(
    model="gemini-2.5-flash", contents="quanto tempo os alunos de DS deveriam ter de intervalo?" \
    "?"
)
print(response.text)

