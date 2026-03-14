import requests
import os
from dotenv import load_dotenv

# 1. Destranca o cofre
load_dotenv()

# 2. Pega todas as chaves
TOKEN = os.getenv("TOKEN_TELEGRAM")
CHAT_ID = os.getenv("CHAT_ID")
API_KEY_CLIMA = os.getenv("API_KEY_CLIMA")

# 3. Cidade alvo do seu projeto
CIDADE = "São Mateus,BR"

print("Lendo os satélites de clima...")

# 4. Viagem 1: Pede os dados para o OpenWeatherMap (GET)
url_clima = f"http://api.openweathermap.org/data/2.5/weather?q={CIDADE}&appid={API_KEY_CLIMA}&units=metric&lang=pt_br"
resposta_clima = requests.get(url_clima)
dados_clima = resposta_clima.json() # Transforma em dicionário (gavetas)

# --- SISTEMA DE PROTEÇÃO (NOVO) ---
if resposta_clima.status_code != 200:
    print("Atenção! O OpenWeatherMap recusou o acesso. A carta que eles mandaram foi:")
    print(dados_clima)
    exit() # O comando exit() desliga o robô aqui para não dar aquele erro vermelho
# ----------------------------------

# 5. Abre as gavetas do dicionário e pega os valores exatos
condicao = dados_clima['weather'][0]['description']
temperatura = dados_clima['main']['temp']
umidade = dados_clima['main']['humidity']

# 6. Prepara o formulário pro Telegram
boletim = (
    f"🌤️ Boletim Tático do Terreno ({CIDADE}):\n\n"
    f"Condição: {condicao.capitalize()}\n"
    f"Temperatura: {temperatura}°C\n"
    f"Umidade do ar: {umidade}%\n\n"
    f"Análise: Planeje o nível de captação de água e a exposição da horta (cebolinhas!) de acordo com o cenário acima!"
)

url_telegram = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
payload = {
    "chat_id": CHAT_ID,
    "text": boletim
}

# 7. Viagem 2: Envia a mensagem pro seu celular (POST)
resposta_telegram = requests.post(url_telegram, data=payload)

if resposta_telegram.status_code == 200:
    print("Boletim meteorológico enviado com sucesso pro celular!")
else:
    print(f"Erro ao enviar: {resposta_telegram.text}")