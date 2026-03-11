import requests

# 1. Suas credenciais
TOKEN = "8667056869:AAEQMTogicmMwZUIMOJb4wuFNvFZnLoYsrU"
CHAT_ID = "1672509128"

# 2. A mensagem que o robô vai enviar
mensagem = "Olá, chefe! Meu ambiente virtual está configurado e eu estou vivo!"

# 3. A URL da API do Telegram para enviar mensagens (Endpoint)
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

# 4. O "pacote" de dados que vamos enviar (para quem e o quê)
payload = {
    "chat_id": CHAT_ID,
    "text": mensagem
}

# 5. Fazendo o disparo da requisição para a internet (Método POST)
resposta = requests.post(url, data=payload)

# 6. Imprimindo o resultado no terminal para a gente ver se deu certo
if resposta.status_code == 200:
    print("Sucesso! Olhe o seu celular.")
else:
    print("Opa, deu algum erro na matriz:")
    print(resposta.text)