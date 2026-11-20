# Referencia de la API

## Configuración

El proxy se comporta como la API de OpenAI. Lo único que cambia es la URL base y la clave.

```python
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    base_url=f'{os.getenv("PROXY_URL")}/v1',
    api_key=os.getenv("API_KEY"),
)
```

Las variables `PROXY_URL` y `API_KEY` se configuran en tu archivo `.env`. Los organizadores te darán los valores el día del taller.

## Endpoints disponibles

### GET /health

Comprueba que el proxy está activo. No requiere autenticación.

```bash
curl $PROXY_URL/health
```

### GET /v1/models

Lista los modelos disponibles. Requiere la API key.

```bash
curl -H "Authorization: Bearer $API_KEY" $PROXY_URL/v1/models
```

### POST /v1/chat/completions

El endpoint principal. Envía una conversación y recibe la respuesta del modelo.

```python
respuesta = client.chat.completions.create(
    model="gemini-3.8-flash",
    messages=[
        {"role": "system", "content": "Eres un tutor educativo."},
        {"role": "user", "content": "Explica qué es una red neuronal."},
    ],
    extra_body={
        "metadata": {
            "request_type": "dev"  # Cambiar a "app" para la entrega
        }
    },
)

print(respuesta.choices[0].message.content)
```

## Modelos disponibles

| Modelo | Descripción | Caso de uso recomendado |
|--------|-------------|------------------------|
| `gemini-3.8-flash` | Rápido, multimodal | Desarrollo, pruebas, iteración rápida |
| `gemini-4-argon` | Potente, multimodal | Respuestas finales, demo, tareas complejas |
| `deepseek-v4.1-flash` | Código y razonamiento (MaaS vía Vertex AI) | Generación de código, lógica paso a paso |
| `glm-5.2` | Alternativa multimodal (MaaS vía Vertex AI) | Diversidad de modelos, comparativas |

## Metadata obligatoria

Todas las peticiones deben incluir `metadata.request_type` en el cuerpo de la petición. Sin este campo, el proxy rechazará la petición con un error.

Valores válidos:
- `"dev"` - para desarrollo y pruebas durante el taller
- `"app"` - para la versión final de tu tutor

```python
extra_body={
    "metadata": {
        "request_type": "dev"
    }
}
```

## Límites

Cada clave de estudiante tiene los siguientes límites:

| Límite | Valor |
|--------|-------|
| Peticiones por minuto (RPM) | 15 |
| Peticiones paralelas | 5 |
| Presupuesto del equipo | $25 USD equivalente |

Si alcanzas el límite de RPM, espera unos segundos antes de reintentar. Si tu equipo agota el presupuesto, contacta a un organizador.

## Errores comunes

### 401 Unauthorized

```
Error: AuthenticationError - Incorrect API key provided
```

**Solución:** Comprueba que tu `.env` tiene la API_KEY correcta y que estás cargando el archivo con `load_dotenv()`.

### 400 Bad Request - Metadata faltante

```
Error: metadata.request_type is required and must be "dev" or "app"
```

**Solución:** Añade `extra_body={"metadata": {"request_type": "dev"}}` a tu llamada `client.chat.completions.create()`.

### 429 Too Many Requests

```
Error: Rate limit reached for model
```

**Solución:** Estás haciendo demasiadas peticiones por minuto. Espera unos segundos e intenta de nuevo. Añade un `time.sleep(1)` entre peticiones si las haces en bucle.

### 422 Budget Exceeded

```
Error: Budget has been exceeded
```

**Solución:** Tu equipo ha agotado el presupuesto asignado. Habla con un organizador.

### Timeout

```
Error: Connection timed out
```

**Solución:** El modelo está tardando mucho en responder. Prueba con un modelo más rápido (`gemini-3.8-flash`) o reduce la longitud del prompt.
