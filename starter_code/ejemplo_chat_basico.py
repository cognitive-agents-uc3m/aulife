"""
ejemplo_chat_basico.py — Llamada mínima al proxy LiteLLM

Qué hace:
    Conecta con un proxy LiteLLM (compatible con la API de OpenAI),
    envía un mensaje sencillo y muestra la respuesta del modelo.
    Incluye un system prompt de tutor educativo y el metadata obligatorio.

Dependencias:
    pip install openai python-dotenv

Cómo ejecutarlo:
    python ejemplo_chat_basico.py

Configuración:
    Crea un archivo .env en esta misma carpeta (ver .env.ejemplo) con:
        PROXY_URL   → URL del proxy LiteLLM
        API_KEY     → tu clave de API

    Consulta los modelos disponibles con:
        curl $PROXY_URL/v1/models -H "Authorization: Bearer $API_KEY"
"""

import os
from dotenv import load_dotenv
from openai import OpenAI

# ── Cargar variables de entorno ──────────────────────────────────────────────
load_dotenv()

PROXY_URL = os.getenv("PROXY_URL", "http://localhost:4000")
API_KEY = os.getenv("API_KEY", "sk-tu-clave-aqui")

# Modelo por defecto. Puedes cambiarlo por cualquiera de los disponibles
# en el proxy (llama a GET /v1/models para verlos).
MODEL = os.getenv("MODEL", "gemini-3.8-flash")

# ── Crear el cliente apuntando al proxy ──────────────────────────────────────
cliente = OpenAI(
    base_url=f"{PROXY_URL}/v1",
    api_key=API_KEY,
)

# ── Definir los mensajes ─────────────────────────────────────────────────────
# El system prompt establece el rol del modelo como tutor educativo.
# El mensaje del usuario es una pregunta sencilla para probar la conexión.
mensajes = [
    {
        "role": "system",
        "content": (
            "Eres un tutor educativo amable y paciente. "
            "Explicas los conceptos de forma clara, con ejemplos cotidianos, "
            "y adaptas tu lenguaje al nivel del estudiante."
        ),
    },
    {
        "role": "user",
        "content": "¿Qué es la inteligencia artificial? Explícamelo como si tuviera 12 años.",
    },
]

# ── Hacer la petición al modelo ──────────────────────────────────────────────
# extra_body incluye el metadata obligatorio para el proxy.
print(f"Enviando petición a {MODEL} vía {PROXY_URL}...\n")

respuesta = cliente.chat.completions.create(
    model=MODEL,
    messages=mensajes,
    extra_body={
        "metadata": {
            "request_type": "dev",
            "tags": ["taller", "starter", "chat-basico"],
        }
    },
)

# ── Mostrar la respuesta ─────────────────────────────────────────────────────
texto = respuesta.choices[0].message.content
print("═" * 60)
print("RESPUESTA DEL MODELO:")
print("═" * 60)
print(texto)
print("═" * 60)

# ── Información adicional (tokens usados) ────────────────────────────────────
if respuesta.usage:
    print(f"\nTokens usados → entrada: {respuesta.usage.prompt_tokens}, "
          f"salida: {respuesta.usage.completion_tokens}, "
          f"total: {respuesta.usage.total_tokens}")
