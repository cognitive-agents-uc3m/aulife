"""
ejemplo_voz.py — Grabar audio del micrófono y enviarlo al modelo

Qué hace:
    Graba audio desde el micrófono durante N segundos, lo guarda como WAV
    temporal, lo codifica en base64 y lo envía al modelo como contenido
    multimodal de tipo audio. El modelo escucha el audio y responde
    describiendo o transcribiendo lo que ha oído.

Dependencias:
    pip install openai python-dotenv sounddevice scipy

Cómo ejecutarlo:
    python ejemplo_voz.py

    El script preguntará cuántos segundos quieres grabar (por defecto 5).

Configuración:
    Crea un archivo .env en esta misma carpeta (ver .env.ejemplo) con:
        PROXY_URL   → URL del proxy LiteLLM
        API_KEY     → tu clave de API

    Consulta los modelos disponibles con:
        curl $PROXY_URL/v1/models -H "Authorization: Bearer $API_KEY"

Nota:
    Necesitas tener un micrófono conectado y accesible. En macOS puede que
    el sistema te pida permiso para acceder al micrófono la primera vez.
"""

import os
import base64
import tempfile
from dotenv import load_dotenv
from openai import OpenAI

# Estas importaciones pueden fallar si no están instaladas.
# El bloque try/except da un mensaje claro de qué instalar.
try:
    import sounddevice as sd
except ImportError:
    print("Falta la librería 'sounddevice'. Instálala con:")
    print("    pip install sounddevice")
    raise SystemExit(1)

try:
    from scipy.io import wavfile
except ImportError:
    print("Falta la librería 'scipy'. Instálala con:")
    print("    pip install scipy")
    raise SystemExit(1)

import numpy as np

# ── Cargar variables de entorno ──────────────────────────────────────────────
load_dotenv()

PROXY_URL = os.getenv("PROXY_URL", "http://localhost:4000")
API_KEY = os.getenv("API_KEY", "sk-tu-clave-aqui")

# Modelo por defecto. Puedes cambiarlo por cualquiera de los disponibles
# en el proxy (llama a GET /v1/models para verlos).
MODEL = os.getenv("MODEL", "gemini-3.8-flash")

# Frecuencia de muestreo estándar para grabación de voz
SAMPLE_RATE = 16000


def grabar_audio(duracion_segundos: int) -> np.ndarray:
    """
    Graba audio desde el micrófono durante la duración indicada.
    Devuelve un array NumPy con las muestras de audio.
    """
    print(f"\n>>> Grabando {duracion_segundos} segundos... ¡Habla ahora!")
    print("   (Pulsa Ctrl+C para cancelar)\n")

    audio = sd.rec(
        frames=int(duracion_segundos * SAMPLE_RATE),
        samplerate=SAMPLE_RATE,
        channels=1,      # Mono es suficiente para voz
        dtype="int16",    # 16 bits, formato estándar para WAV
    )
    sd.wait()  # Esperar a que termine la grabación

    print("   Grabación completada.\n")
    return audio


def guardar_wav_temporal(audio: np.ndarray, sample_rate: int) -> str:
    """
    Guarda el audio en un archivo WAV temporal y devuelve su ruta.
    """
    archivo_temp = tempfile.NamedTemporaryFile(
        suffix=".wav", delete=False
    )
    wavfile.write(archivo_temp.name, sample_rate, audio)
    archivo_temp.close()
    return archivo_temp.name


def codificar_audio_base64(ruta_wav: str) -> str:
    """
    Lee un archivo WAV y devuelve su contenido codificado en base64.
    """
    with open(ruta_wav, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")


def main():
    # ── Preguntar duración de la grabación ───────────────────────────────
    entrada = input("¿Cuántos segundos quieres grabar? [5]: ").strip()
    if entrada == "":
        duracion = 5
    else:
        try:
            duracion = int(entrada)
            if duracion < 1:
                print("La duración mínima es 1 segundo. Usando 1.")
                duracion = 1
            elif duracion > 60:
                print("La duración máxima es 60 segundos. Usando 60.")
                duracion = 60
        except ValueError:
            print("Valor no válido. Usando 5 segundos por defecto.")
            duracion = 5

    # ── Grabar audio ─────────────────────────────────────────────────────
    audio = grabar_audio(duracion)

    # ── Guardar como WAV temporal ────────────────────────────────────────
    ruta_wav = guardar_wav_temporal(audio, SAMPLE_RATE)
    print(f"Audio guardado temporalmente en: {ruta_wav}")

    # ── Codificar en base64 ──────────────────────────────────────────────
    audio_b64 = codificar_audio_base64(ruta_wav)
    print(f"Audio codificado en base64 ({len(audio_b64)} caracteres)")

    # ── Crear el cliente apuntando al proxy ──────────────────────────────
    cliente = OpenAI(
        base_url=f"{PROXY_URL}/v1",
        api_key=API_KEY,
    )

    # ── Construir el mensaje multimodal con audio ────────────────────────
    # Se envía el audio directamente al modelo como input_audio en formato WAV.
    # El modelo procesará el audio y responderá con texto.
    mensajes = [
        {
            "role": "user",
            "content": [
                {
                    "type": "input_audio",
                    "input_audio": {
                        "data": audio_b64,
                        "format": "wav",
                    },
                },
                {
                    "type": "text",
                    "text": (
                        "Escucha el audio que te envío. "
                        "Transcribe lo que se dice y, si es posible, "
                        "indica el idioma detectado."
                    ),
                },
            ],
        }
    ]

    # ── Hacer la petición al modelo ──────────────────────────────────────
    print(f"\nEnviando audio a {MODEL} vía {PROXY_URL}...\n")

    respuesta = cliente.chat.completions.create(
        model=MODEL,
        messages=mensajes,
        extra_body={
            "metadata": {
                "request_type": "dev",
                "tags": ["taller", "starter", "voz"],
            }
        },
    )

    # ── Mostrar la respuesta ─────────────────────────────────────────────
    texto = respuesta.choices[0].message.content
    print("═" * 60)
    print("RESPUESTA DEL MODELO:")
    print("═" * 60)
    print(texto)
    print("═" * 60)

    # ── Información adicional (tokens usados) ────────────────────────────
    if respuesta.usage:
        print(f"\nTokens usados → entrada: {respuesta.usage.prompt_tokens}, "
              f"salida: {respuesta.usage.completion_tokens}, "
              f"total: {respuesta.usage.total_tokens}")

    # ── Limpiar el archivo temporal ──────────────────────────────────────
    try:
        os.unlink(ruta_wav)
        print(f"\nArchivo temporal eliminado: {ruta_wav}")
    except OSError:
        pass


if __name__ == "__main__":
    main()
