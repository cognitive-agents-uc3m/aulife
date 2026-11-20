#!/usr/bin/env python3
"""
multimodal.py -- Ejemplo de llamada multimodal (imagen + texto).
Envía una imagen al modelo y pide que la analice.

Uso:
    python multimodal.py ruta/a/imagen.png "Explica este diagrama"

Configuración:
    Crea un archivo .env en esta misma carpeta (ver .env.ejemplo) con:
        PROXY_URL   → URL del proxy LiteLLM
        API_KEY     → tu clave de API

    Consulta los modelos disponibles con:
        curl $PROXY_URL/v1/models -H "Authorization: Bearer $API_KEY"
"""

import os
import sys
import base64
from openai import OpenAI

PROXY_URL = os.getenv("PROXY_URL", "https://aulife-proxy-66041181251.europe-west1.run.app")
API_KEY = os.getenv("API_KEY", "")

# Modelo por defecto. Puedes cambiarlo por cualquiera de los disponibles
# en el proxy (llama a GET /v1/models para verlos).
MODEL = os.getenv("MODEL", "gemini-3.8-flash")

client = OpenAI(
    base_url=f"{PROXY_URL}/v1",
    api_key=API_KEY,
)


def codificar_imagen(ruta: str) -> str:
    """Lee una imagen y la codifica en base64."""
    with open(ruta, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")


def detectar_tipo_mime(ruta: str) -> str:
    """Detecta el tipo MIME de la imagen por extensión."""
    ext = os.path.splitext(ruta)[1].lower()
    tipos = {
        ".png": "image/png",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".gif": "image/gif",
        ".webp": "image/webp",
    }
    return tipos.get(ext, "image/png")


def analizar_imagen(ruta_imagen: str, pregunta: str) -> str:
    """
    Envía una imagen junto con una pregunta al modelo.

    Args:
        ruta_imagen: ruta al archivo de imagen
        pregunta: qué quieres saber sobre la imagen

    Devuelve la respuesta del modelo.
    """
    imagen_b64 = codificar_imagen(ruta_imagen)
    tipo_mime = detectar_tipo_mime(ruta_imagen)

    respuesta = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": "Eres un tutor de IA. Analiza las imágenes que "
                           "te envían los estudiantes (diagramas, gráficas, "
                           "capturas de código) y explícalas con claridad.",
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": pregunta,
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:{tipo_mime};base64,{imagen_b64}"
                        },
                    },
                ],
            },
        ],
        max_tokens=1024,
        extra_body={
            "metadata": {
                "request_type": "dev",
                "tags": ["dev"]
            }
        },
    )

    return respuesta.choices[0].message.content


def main():
    if len(sys.argv) < 2:
        print("Uso: python multimodal.py <imagen> [pregunta]")
        print('Ejemplo: python multimodal.py diagrama.png "¿Qué muestra este diagrama?"')
        sys.exit(1)

    ruta_imagen = sys.argv[1]
    pregunta = " ".join(sys.argv[2:]) if len(sys.argv) > 2 else "Describe y explica esta imagen."

    if not os.path.exists(ruta_imagen):
        print(f"Error: no se encuentra '{ruta_imagen}'")
        sys.exit(1)

    print(f"Analizando '{ruta_imagen}'...")
    print(f"Pregunta: {pregunta}\n")

    respuesta = analizar_imagen(ruta_imagen, pregunta)
    print(f"Tutor > {respuesta}")


if __name__ == "__main__":
    main()
