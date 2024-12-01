# Generador-de-historia-en-Python-con-la-API-de-Generation-Text-WebUI

## Descripción

Este proyecto permite generar historias de manera automática utilizando la API de la aplicación <a href="https://github.com/oobabooga/text-generation-webui">**Generation Text WebUI**</a>. El programa está escrito en **Python** y solicita al usuario ciertos datos para crear una narrativa personalizada. Los datos solicitados incluyen:

- Nombre del personaje principal
- Nombre del personaje secundario
- Lugar donde transcurre el relato
- Una acción importante que debe acontecer en la historia

Además, el programa permite ajustar parámetros como la **temperatura** (para controlar la creatividad de la historia) y proporciona diferentes **Modelos de Lenguaje (LLM)** para comparar y generar la mejor historia posible.

Este proyecto fue desarrollado como parte del **Máster de FP en Inteligencia Artificial y Big Data**.

## Requisitos
Para ejecutar este proyecto, necesitarás tener instalado lo siguiente:

- **Python 3.x** o superior
- **requests**: Para realizar solicitudes HTTP a la API.
- **python-dotenv**: Para cargar las variables de entorno desde el archivo `.env`.

Puedes instalar las dependencias ejecutando:

```bash
pip install requests python-dotenv
```

## 1. Configuración de la API
Puedes canviar os.getenv("API_URL") por tu url, y {os.getenv('API_TOKEN')} por tu token si lo has puesto en la api, o tenr API_URL y API_TOKEN en el fichero .env, si no usaa token puedes eliminar la linea "Authorization": f"Bearer {os.getenv('API_TOKEN')}" # Token o clave secreta y dejar solo "Content-Type": "application/json" en headers.

## 2. Ejecución del programa
Para ejecutar el generador de historias, simplemente corre el siguiente comando:

python chat.py

El programa te pedirá que ingreses lo siguiente:

Nombre del personaje principal
Nombre del personaje secundario
Lugar donde transcurre la historia
Una acción importante que debe suceder en la historia

Además, podrás seleccionar el nivel de creatividad (temperatura) de la historia, con un valor float cuanto mas alto mas creativo, mejor no subir mucho de 1.0 puede llegar a inventar palabras.

## 4. Selección de modelos
El programa también permite seleccionar diferentes Modelos de Lenguaje (LLMs), como:

Qwen_Qwen2.5-1.5B-Instruct
Qwen_Qwen2.5-0.5B-Instruct
EleutherAI_gpt-neo-1.3B
Cada modelo tiene características diferentes, lo que afecta la creatividad y precisión de las historias generadas.
Si en tu api tines modelos distintos solo debes modificar el diccionario.

## Ejemplos de historias generadas
Ejemplo 1:
* Modelo: Qwen_Qwen2.5-1.5B-Instruct
* Temperatura: 1.0
* Nombre del personaje principal: Alice
* Nombre del personaje secundario: Bob
* Lugar: Wonderland
* Acción: Descubren un portal mágico

<img /images/ejemplo_1.png>

Ejemplo 2:
* Modelo: Qwen_Qwen2.5-0.5B-Instruct
* Temperatura: 0.7
* Nombre del personaje principal: John
* Nombre del personaje secundario: Sarah
* Lugar: New York
* Acción: Salvan la ciudad de un desastre

<img /images/ejemplo_2.png>

Ejemplo 3:
* Modelo: EleutherAI_gpt-neo-1.3B
* Temperatura: 0.4
* Nombre del personaje principal: Emma
* Nombre del personaje secundario: Liam
* Lugar: Paris
* Acción: Encuentran un tesoro escondido

<img /images/ejemplo_3.png>
