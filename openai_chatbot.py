import os
import openai
from dotenv import load_dotenv

# Cargar la API Key de OpenAI desde el archivo .env
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Inicializar cliente OpenAI
client = openai.OpenAI(api_key=api_key)

def chat_with_openai(user_input, chat_history):

    # Agregar mensaje del usuario al historial
    chat_history.append({"role": "user", "content": user_input})

    # Llamar a la API de OpenAI
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=chat_history
    )

    # Obtener la respuesta del asistente y la agregamos al historial
    assistant_response = response.choices[0].message.content
    chat_history.append({"role": "assistant", "content": assistant_response})

    return assistant_response, chat_history

# Ejecutar el chatbot en la consola
if __name__ == "__main__":
    chat_history = [{"role": "system", "content": "You are a helpful assistant."}]
    
    print("💬 Chatbot iniciado. Escribe 'salir' para terminar.")
    
    while True:
        user_input = input("Tú: ")
        if user_input == "salir":
            print("👋 Adiós!")
            break
        response, chat_history = chat_with_openai(user_input, chat_history)
        print(f"Bot: {response}\n")
