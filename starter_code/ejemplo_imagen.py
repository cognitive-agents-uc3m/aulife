"""
ejemplo_imagen.py — Enviar una imagen al modelo y hacerle preguntas sobre ella

Qué hace:
    Carga una imagen local, la codifica en base64 y la envía al modelo
    como contenido multimodal junto con una pregunta. El modelo analiza
    la imagen y responde describiendo lo que ve.

Dependencias:
    pip install openai python-dotenv

Cómo ejecutarlo:
    python ejemplo_imagen.py ruta/a/tu/imagen.png

    Si no se pasa ningún argumento, el script mostrará instrucciones de uso.

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
import mimetypes
from dotenv import load_dotenv
from openai import OpenAI

# ── Cargar variables de entorno ──────────────────────────────────────────────
load_dotenv()

PROXY_URL = os.getenv("PROXY_URL", "http://localhost:4000")
API_KEY = os.getenv("API_KEY", "sk-tu-clave-aqui")

# Modelo por defecto. Puedes cambiarlo por cualquiera de los disponibles
# en el proxy (llama a GET /v1/models para verlos).
MODEL = os.getenv("MODEL", "gemini-3.8-flash")


def cargar_imagen_base64(ruta: str) -> tuple[str, str]:
    """
    Lee un archivo de imagen y devuelve su contenido en base64
    junto con su tipo MIME (por ejemplo, "image/png").
    """
    if not os.path.isfile(ruta):
        print(f"Error: no se encontró el archivo '{ruta}'")
        sys.exit(1)

    # Detectar el tipo MIME a partir de la extensión
    tipo_mime, _ = mimetypes.guess_type(ruta)
    if tipo_mime is None or not tipo_mime.startswith("image/"):
        print(f"Error: el archivo '{ruta}' no parece ser una imagen válida.")
        print("Formatos aceptados: PNG, JPG, JPEG, GIF, WEBP")
        sys.exit(1)

    with open(ruta, "rb") as f:
        datos_base64 = base64.b64encode(f.read()).decode("utf-8")

    return datos_base64, tipo_mime


def main():
    # ── Comprobar que se ha pasado una imagen como argumento ─────────────
    if len(sys.argv) < 2:
        print("Uso: python ejemplo_imagen.py <ruta_imagen>")
        print()
        print("Ejemplo:")
        print("    python ejemplo_imagen.py foto.png")
        print("    python ejemplo_imagen.py captura.jpg")
        print()
        print("El script enviará la imagen al modelo y este describirá lo que ve.")
        sys.exit(0)

    ruta_imagen = sys.argv[1]
    print(f"Cargando imagen: {ruta_imagen}")

    # ── Codificar la imagen en base64 ────────────────────────────────────
    imagen_b64, tipo_mime = cargar_imagen_base64(ruta_imagen)
    print(f"Imagen cargada correctamente ({tipo_mime})")

    # ── Crear el cliente apuntando al proxy ──────────────────────────────
    cliente = OpenAI(
        base_url=f"{PROXY_URL}/v1",
        api_key=API_KEY,
    )

    # ── Construir el mensaje multimodal ──────────────────────────────────
    # El contenido del usuario incluye tanto la imagen como la pregunta.
    # La imagen se envía como data URI en base64.
    mensajes = [
        {
            "role": "user",
            "content": [
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:{tipo_mime};base64,{imagen_b64}",
                    },
                },
                {
                    "type": "text",
                    "text": (
                        "Describe detalladamente lo que ves en esta imagen. "
                        "Incluye los elementos principales, colores y cualquier "
                        "texto que aparezca."
                    ),
                },
            ],
        }
    ]

    # ── Hacer la petición al modelo ──────────────────────────────────────
    print(f"\nEnviando imagen a {MODEL} vía {PROXY_URL}...\n")

    respuesta = cliente.chat.completions.create(
        model=MODEL,
        messages=mensajes,
        extra_body={
            "metadata": {
                "request_type": "dev",
                "tags": ["taller", "starter", "imagen"],
            }
        },
    )

    # ── Mostrar la respuesta ─────────────────────────────────────────────
    texto = respuesta.choices[0].message.content
    print("═" * 60)
    print("DESCRIPCIÓN DEL MODELO:")
    print("═" * 60)
    print(texto)
    print("═" * 60)

    # ── Información adicional (tokens usados) ────────────────────────────
    if respuesta.usage:
        print(f"\nTokens usados → entrada: {respuesta.usage.prompt_tokens}, "
              f"salida: {respuesta.usage.completion_tokens}, "
              f"total: {respuesta.usage.total_tokens}")


if __name__ == "__main__":
    main()
