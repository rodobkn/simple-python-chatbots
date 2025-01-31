import os
import openai
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

client = openai.OpenAI(api_key=api_key)

def chat_with_openai_stream(user_input, chat_history):

    chat_history.append({"role": "user", "content": user_input})

    # Llamar a la API con streaming activado
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=chat_history,
        stream=True  # Activamos streaming
    )

    # Mostrar la respuesta en tiempo real
    assistant_response = ""
    print("Bot: ", end="", flush=True)  # No hacer salto de línea

    for chunk in response:
        if chunk.choices and chunk.choices[0].delta.content:
            text = chunk.choices[0].delta.content
            print(text, end="", flush=True)  # Imprimir sin salto de línea
            assistant_response += text

    print("\n")  # Nueva línea después de la respuesta

    # Agregar la respuesta al historial
    chat_history.append({"role": "assistant", "content": assistant_response})

    return chat_history

# Ejecutar el chatbot en la consola con streaming
if __name__ == "__main__":
    chat_history = [{"role": "system", "content": "You are a helpful assistant."}]
    
    print("💬 Chatbot con streaming iniciado. Escribe 'salir' para terminar.")
    
    while True:
        user_input = input("Tú: ")
        if user_input.lower() == "salir":
            print("👋 Adiós!")
            break
        chat_history = chat_with_openai_stream(user_input, chat_history)
