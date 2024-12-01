import requests
import json
from dotenv import load_dotenv # type: ignore
import os

# Cargar las variables de entorno
load_dotenv()

# Obtener URL y token desde las variables de entorno
url = os.getenv("API_URL")
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {os.getenv('API_TOKEN')}" # Token o clave secreta
}
tokens = 400
stops = ["<END>", "---"]

# Modelos disponibles
modelos = {
    "a": "Qwen_Qwen2.5-1.5B-Instruct",
    "b": "Qwen_Qwen2.5-0.5B-Instruct",
    "c": "EleutherAI_gpt-neo-1.3B"
}

# Función para generar la historia
def generar_historia(prompt, max_tokens=tokens, stop=stops, modelo="Qwen_Qwen2.5-0.5B-Instruct", temp=1.0):
    body = {
        "model": modelo,
        "prompt": prompt,
        "max_tokens": max_tokens,
        "stop": stop,
        "temperature": temp,
        "echo": False 
    }

    try:
        response = requests.post(url=url, headers=headers, json=body)
        response.raise_for_status()
        response_data = response.json()
        return response_data["choices"][0]["text"].strip()
    except requests.exceptions.HTTPError as e:
        print(f"Error HTTP: {e.response.status_code} - {e.response.reason}")
        if e.response.status_code == 500:
            print("Error interno del servidor. Verifica los logs del servidor para más detalles.")
    except requests.exceptions.RequestException as e:
        print(f"Error en la solicitud: {e}")
    except json.JSONDecodeError:
        print("Error al decodificar la respuesta JSON.")
    except KeyError:
        print("Error: La respuesta no contiene el formato esperado.")
    except Exception as e:
        print(f"Error inesperado: {e}")
    return None

# Función para seleccionar el modelo
def seleccionar_modelo():
    while True:
        print("Elige el modelo de lenguaje que deseas usar:")
        for key, value in modelos.items():
            print(f"{key}) {value}")
        opcion_modelo = input("Introduce la letra correspondiente a tu elección: ").lower()
        if opcion_modelo in modelos:
            return modelos[opcion_modelo]
        else:
            print("Opción no válida. Por favor, elige una opción válida.")

# Llamar a la función para seleccionar el modelo
modelo = seleccionar_modelo()

try:
    temp = float(input("Elige la temperatura que deseas usar (ej. 0.7): "))
except ValueError:
    print("Temperatura inválida. Se utilizará el valor por defecto (1.0).")
    temp = 1.0

nombre_personaje_principal = input("Introduce el nombre del personaje principal: ")
nombre_personaje_secundario = input("Introduce el nombre del personaje secundario: ")
lugar = input("Introduce el lugar donde transcurre la historia: ")
accion = input("Introduce una acción importante que debe acontecer en la historia: ")

prompt = f"Una historia sobre {nombre_personaje_principal}, el personaje principal y {nombre_personaje_secundario}, el personaje secundario en {lugar}, donde {accion}. Habla unicamente de la historia."

assistant_message = generar_historia(prompt, max_tokens=tokens, stop=stops, modelo=modelo, temp=temp)

if assistant_message:
    print("Historia generada:")
    print(assistant_message)
else:
    print("No se pudo generar la historia.")
print("\n")
