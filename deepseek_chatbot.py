import os
import openai
from dotenv import load_dotenv

# Cargar la API Key de DeepSeek desde el archivo .env
load_dotenv()
api_key = os.getenv("DEEPSEEK_API_KEY")

# Inicializar cliente OpenAI apuntando a los servidores de DeepSeek
client = openai.OpenAI(api_key=api_key, base_url="https://api.deepseek.com")

def chat_with_deepseek(user_input, chat_history):
    chat_history.append({"role": "user", "content": user_input})

    # Llamar a la API de DeepSeek
    response = client.chat.completions.create(
        model="deepseek-chat",  # Modelo de DeepSeek
        messages=chat_history
    )

    assistant_response = response.choices[0].message.content
    chat_history.append({"role": "assistant", "content": assistant_response})

    return assistant_response, chat_history

if __name__ == "__main__":
    chat_history = [{"role": "system", "content": "You are a helpful assistant."}]
    
    print("💬 Chatbot (DeepSeek) iniciado. Escribe 'salir' para terminar.")
    
    while True:
        user_input = input("Tú: ")
        if user_input == "salir":
            print("👋 Adiós!")
            break
        response, chat_history = chat_with_deepseek(user_input, chat_history)
        print(f"Bot: {response}\n")
