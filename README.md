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
Api:
- 

Para ejecutar este proyecto, necesitarás tener instalado lo siguiente:

- **Python 3.x** o superior
- **requests**: Para realizar solicitudes HTTP a la API.
- **python-dotenv**: Para cargar las variables de entorno desde el archivo `.env`.

Puedes instalar las dependencias ejecutando:

```bash
pip install requests python-dotenv
