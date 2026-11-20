# Write-up: [Nombre del equipo]

> Aulife -- Noviembre 2026
> Universidad Carlos III de Madrid

## 1. Enfoque y arquitectura

Describid brevemente cómo habéis planteado el tutor virtual:
- ¿Qué hace vuestro tutor que lo diferencia del starter code?
- ¿Cuál es la arquitectura general? (diagrama opcional)
- ¿Cómo fluye una pregunta del estudiante hasta la respuesta?

## 2. Decisiones técnicas

### Modelo elegido
- ¿Qué modelo(s) habéis usado (`gemini-3.8-flash`, `gemini-4-argon`, `deepseek-v4.1-flash`, `glm-5.2`)? ¿Por qué?
- ¿Habéis ajustado parámetros como `temperature` o `max_tokens`?

### Método de búsqueda en el corpus
- ¿Habéis mantenido la búsqueda por palabras del starter code o la habéis mejorado?
- Si la habéis mejorado, ¿qué método habéis usado? (embeddings, TF-IDF, otro)

### Prompt del sistema
- ¿Qué instrucciones le dais al modelo en el prompt del sistema?
- ¿Habéis iterado sobre el prompt? ¿Qué cambios habéis notado?

### Interfaz de usuario
- ¿Terminal, web (Gradio/Streamlit/Flask) u otra?
- ¿Por qué habéis elegido esa interfaz?

### Formatos de corpus procesados
- ¿Qué formatos habéis integrado? (PDF, texto, web, vídeo, imágenes)
- ¿Cómo habéis extraído la información de cada formato?

## 3. Despliegue

- ¿Cómo se ejecuta vuestro proyecto?
- ¿Habéis incluido Dockerfile, Makefile u otro script de automatización?

## 4. Resultados

Incluid al menos 3 ejemplos de interacción con el tutor
(pregunta del estudiante y respuesta generada):

### Ejemplo 1
- **Pregunta:** [pregunta del estudiante]
- **Respuesta del tutor:** [respuesta generada]
- **Valoración:** [¿La respuesta es correcta? ¿Es útil? ¿Es clara?]

### Ejemplo 2
- **Pregunta:** [pregunta del estudiante]
- **Respuesta del tutor:** [respuesta generada]
- **Valoración:** [valoración breve]

### Ejemplo 3
- **Pregunta:** [pregunta del estudiante]
- **Respuesta del tutor:** [respuesta generada]
- **Valoración:** [valoración breve]

## 5. Dificultades encontradas

- ¿Qué problemas habéis tenido durante el desarrollo?
- ¿Cómo los habéis resuelto (o no)?

## 6. Posibles mejoras

- Si tuvierais más tiempo, ¿qué haríais de forma diferente?
- ¿Qué funcionalidades añadiríais?

## 7. Conclusiones

- ¿Qué habéis aprendido?
- ¿Qué os ha sorprendido del proceso?
