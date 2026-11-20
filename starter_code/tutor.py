#!/usr/bin/env python3
"""
tutor.py -- Ejemplo de tutor virtual con IA para el aula.
Aulife, noviembre 2026.

Este es un ejemplo de punto de entrada. Conecta con el proxy LiteLLM
y permite hacer preguntas sobre el corpus de documentos.

CÓMO FUNCIONA:
1. Carga los documentos del corpus.
2. Cuando el usuario hace una pregunta, busca los fragmentos relevantes.
3. Envía la pregunta + contexto al modelo de IA.
4. Muestra la respuesta.

QUÉ PUEDES MEJORAR (ideas para el taller):
- Interfaz web con Gradio, Streamlit, Flask o cualquier framework.
- Búsqueda por embeddings en vez de por palabras.
- Memoria de la conversación (ahora mismo cada pregunta es independiente).
- Soporte multimodal (enviar imágenes/diagramas al modelo).
- Ingesta de más formatos: HTML, vídeos de YouTube, presentaciones.
- Evaluación automática: que el tutor haga preguntas al estudiante.
- Personalización: que el tutor adapte el nivel al estudiante.
- Múltiples asignaturas.
"""

import os
from openai import OpenAI
from cargar_documentos import cargar_corpus, buscar_relevantes

# Cargar configuración desde variables de entorno o archivo .env
# Si usas python-dotenv: from dotenv import load_dotenv; load_dotenv()

PROXY_URL = os.getenv("PROXY_URL", "https://aulife-proxy-66041181251.europe-west1.run.app")
API_KEY = os.getenv("API_KEY", "")

# Modelo por defecto. Consulta los disponibles con:
#   curl $PROXY_URL/v1/models -H "Authorization: Bearer $API_KEY"
MODEL = os.getenv("MODEL", "gemini-3.8-flash")

# Inicializar cliente OpenAI apuntando al proxy
client = OpenAI(
    base_url=f"{PROXY_URL}/v1",
    api_key=API_KEY,
)

# Prompt del sistema para el tutor
SYSTEM_PROMPT = """Eres un tutor virtual universitario especializado en Inteligencia Artificial.

Tu objetivo es ayudar a los estudiantes a comprender los conceptos del curso.

Reglas:
- Responde SOLO en español.
- Basa tus respuestas en el material del curso que se te proporciona como contexto.
- Si la pregunta no está cubierta por el material, dilo honestamente.
- Adapta tu explicación al nivel universitario (grado en informática).
- Usa ejemplos concretos cuando sea posible.
- Si el estudiante parece confundido, intenta explicarlo de otra forma.
- Puedes usar analogías; eso sí, aclara que son simplificaciones.
- Al final de tu respuesta, sugiere una pregunta de seguimiento para profundizar.
"""


def chat_con_contexto(
    pregunta: str,
    documentos: list[dict],
    historial: list[dict] | None = None,
) -> str:
    """
    Envía una pregunta al tutor con contexto del corpus.

    Args:
        pregunta: lo que pregunta el estudiante
        documentos: corpus cargado
        historial: mensajes anteriores (para memoria de conversación)

    Devuelve la respuesta del tutor.
    """
    # Buscar fragmentos relevantes
    contexto = buscar_relevantes(pregunta, documentos)

    # Construir mensajes
    mensajes = [{"role": "system", "content": SYSTEM_PROMPT}]

    # Añadir historial si existe
    if historial:
        mensajes.extend(historial)

    # Añadir la pregunta con contexto
    mensaje_usuario = f"""Pregunta del estudiante: {pregunta}

Material del curso relevante:
{contexto}

Responde basándote en el material proporcionado."""

    mensajes.append({"role": "user", "content": mensaje_usuario})

    # Llamar al modelo (metadata obligatorio: "app" para el tutor final)
    respuesta = client.chat.completions.create(
        model=MODEL,
        messages=mensajes,
        temperature=0.7,
        max_tokens=1024,
        extra_body={
            "metadata": {
                "request_type": "app",
                "tags": ["app"]
            }
        },
    )

    return respuesta.choices[0].message.content


def main():
    """Bucle principal del tutor (interfaz por terminal)."""
    print("=" * 60)
    print("  TUTOR VIRTUAL DE INTELIGENCIA ARTIFICIAL")
    print("  Aulife -- Noviembre 2026")
    print("=" * 60)
    print()

    # Cargar corpus
    print("Cargando documentos del curso...")
    documentos = cargar_corpus("corpus")
    print()

    # Historial de conversación
    historial = []

    print("Escribe tu pregunta (o 'salir' para terminar).\n")

    while True:
        pregunta = input("Estudiante > ").strip()

        if not pregunta:
            continue
        if pregunta.lower() in ("salir", "exit", "quit"):
            print("\nHasta la próxima. Sigue aprendiendo.")
            break

        print("\nTutor: Pensando...\n")

        try:
            respuesta = chat_con_contexto(pregunta, documentos, historial)
            print(f"Tutor > {respuesta}\n")

            # Guardar en historial
            historial.append({"role": "user", "content": pregunta})
            historial.append({"role": "assistant", "content": respuesta})

            # Limitar historial a las últimas 10 interacciones
            if len(historial) > 20:
                historial = historial[-20:]

        except Exception as e:
            print(f"Error al contactar con el modelo: {e}\n")
            print("Comprueba tu conexión y tu clave. Puedes seguir intentando.\n")


if __name__ == "__main__":
    main()
