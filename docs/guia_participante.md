# Guía del participante

Bienvenido al taller **Aulife** de la Semana de la Ciencia 2026 en la Universidad Carlos III de Madrid. Durante las próximas horas construirás un tutor virtual de IA desde cero.

## Requisitos previos

Antes de empezar, asegúrate de tener instalado:

- **Python 3.10 o superior** - comprueba con `python3 --version`
- **git** - comprueba con `git --version`
- **Un editor de código** - VS Code, PyCharm, o cualquier editor con el que te sientas cómodo
- **Una terminal** - la terminal integrada de tu editor vale perfectamente

No necesitas experiencia previa con IA ni con APIs. Todo lo que necesitas saber está en esta guía y en los ejemplos del repositorio.

## Instalación paso a paso

### 1. Clona el repositorio

```bash
git clone https://github.com/cognitive-agents-uc3m/aulife
cd aulife
```

### 2. Crea un entorno virtual

```bash
python3 -m venv .venv
source .venv/bin/activate   # En Windows: .venv\Scripts\activate
```

### 3. Instala las dependencias

```bash
pip install -r starter_code/requirements.txt
```

### 4. Configura tu entorno

Copia el archivo de ejemplo y rellena tus credenciales (te las darán los organizadores):

```bash
cp starter_code/.env.ejemplo starter_code/.env
```

Edita `starter_code/.env` con los valores que te proporcionen:

```
PROXY_URL=https://aulife-proxy-xxxxxxxx.run.app
API_KEY=sk-tu-clave-personal
```

## Verificar la conexión

Ejecuta el script de verificación para comprobar que todo funciona:

```bash
cd starter_code
python3 verificar_setup.py
```

El script comprueba tres cosas: que el proxy responde, que puedes listar los modelos disponibles y que puedes hacer una petición de chat. Si las tres pasan, estás listo.

## Estructura del proyecto

```
starter_code/
  tutor.py                  Tu tutor principal - el archivo que vas a modificar
  cargar_documentos.py      Funciones para cargar y buscar en el corpus
  multimodal.py             Funciones para enviar imágenes al modelo
  ejemplo_chat_basico.py    Ejemplo mínimo de chat con el proxy
  ejemplo_imagen.py         Ejemplo de análisis de imágenes
  ejemplo_voz.py            Ejemplo de entrada por voz
  verificar_setup.py        Script de verificación del setup
  requirements.txt          Dependencias del proyecto
  .env.ejemplo              Plantilla de variables de entorno
corpus/                     Documentos de referencia para tu tutor
  imagenes/                 Imágenes para análisis multimodal
docs/                       Documentación del taller
writeup_plantilla.md        Plantilla para tu informe final
```

## Flujo de trabajo recomendado

1. **Explora el corpus** - Lee los documentos en `corpus/`. Son el conocimiento que tu tutor puede usar para responder preguntas.
2. **Ejecuta los ejemplos** - Prueba `ejemplo_chat_basico.py` y `ejemplo_imagen.py` para entender cómo funciona la API.
3. **Modifica `tutor.py`** - Este es tu archivo principal. Cambia el prompt del sistema, mejora la búsqueda en el corpus, añade funcionalidades.
4. **Prueba iterativamente** - Cada cambio que hagas, ejecuta el tutor y comprueba que las respuestas mejoran.
5. **Documenta** - Ve rellenando `writeup_plantilla.md` mientras trabajas. No lo dejes para el final.

## Modelos disponibles

| Modelo | Velocidad | Calidad | Uso recomendado |
|--------|-----------|---------|-----------------|
| `gemini-3.8-flash` | Muy rápida | Buena | Desarrollo y pruebas rápidas |
| `gemini-4-argon` | Media | Muy alta | Respuestas de calidad, demo final |
| `deepseek-v4.1-flash` | Rápida | Alta en código | Generación de código, razonamiento |
| `glm-5.2` | Media | Buena | Diversidad de modelos, comparativas |

Para desarrollo usa `gemini-3.8-flash` (rápido y barato). Cambia a modelos de mayor calidad para la demo final.

## Consejos importantes

- **Usa `request_type: "dev"` mientras desarrollas.** Cambia a `"app"` solo para la entrega final. Esto nos ayuda a distinguir el tráfico de pruebas del real.
- **No hardcodees la API key.** Siempre léela desde el `.env` con `python-dotenv`. Si subes tu clave a git, se revocará.
- **Revisa los ejemplos antes de escribir código.** `ejemplo_chat_basico.py` tiene todo lo que necesitas para empezar.
- **Empieza simple.** Haz que funcione primero, luego mejora. Un tutor básico que responde bien es mejor que uno complejo que falla.
- **Guarda tu trabajo con git.** Haz commits frecuentes: `git add . && git commit -m "descripción del cambio"`.

## Pedir ayuda

Si te atascas:

1. Revisa los mensajes de error. La mayoría tienen una solución directa (mira `docs/cheatsheet.txt`).
2. Consulta la referencia de la API en `docs/referencia_api.md`.
3. Levanta la mano y pregunta a un mentor. Estamos aquí para ayudarte.

No pierdas tiempo bloqueado. Si llevas más de 10 minutos sin avanzar, pregunta.
