# Criterios de evaluación

## Tabla de criterios

Cada criterio se puntúa de 1 a 5. La puntuación final es la suma ponderada.

| Criterio | Peso | Qué se evalúa |
|----------|------|---------------|
| **Write-up** | 40% | Calidad del documento `writeup.md`: enfoque bien explicado, decisiones técnicas justificadas, resultados documentados con honestidad y reflexión sobre lecciones aprendidas. Se valora especialmente la profundidad del análisis, la capacidad de conectar decisiones con resultados y la utilidad del documento como referencia. |
| **Calidad de las respuestas** | 20% | Precisión, claridad y utilidad de lo que responde el tutor. Las respuestas se apoyan en el corpus proporcionado, no inventan información y proporcionan citas del contenido utilizado. En entradas multimodales (imágenes, gráficos), la respuesta refleja fielmente lo que se observa en el contenido visual. |
| **Capacidad multimodal** | 20% | Integración de más de una modalidad de entrada o salida: texto, voz, imagen, interfaz gráfica, diagramas generados, etc. Se valora especialmente la interacción por voz y el diseño agnóstico a la plataforma. |
| **Demo en vivo** | 20% | Claridad al explicar lo que han construido y por qué. Calidad de los ejemplos elegidos. Que el sistema funcione durante la demo sin caerse: gestión de errores, tiempos de respuesta razonables. |

## Nota sobre la creatividad

La creatividad no aparece como criterio independiente, y al mismo tiempo se valora transversalmente: en la capacidad multimodal (soluciones ingeniosas de integración), en la demo (experiencias que sorprendan) y en el write-up (análisis original de las decisiones tomadas). Ideas como tutorización adaptativa, gamificación, generación de ejercicios, detección de dudas o conversación por voz natural enriquecen la puntuación en los criterios donde se manifiesten.

## Qué se entrega

Cada equipo debe entregar:

1. **Repositorio git** con el código fuente de su tutor. Debe poder ejecutarse siguiendo las instrucciones del README o del writeup.
2. **Writeup** (`writeup_plantilla.md` rellenado) con la descripción del enfoque, decisiones técnicas, resultados y conclusiones.
3. **Demo en vivo** de 3 minutos donde el equipo muestra el tutor funcionando con al menos 3 interacciones reales.

## Bonus

Los siguientes puntos suman puntuación extra sobre la nota base:

- **Uso de múltiples modelos**: el tutor elige el modelo más adecuado según el tipo de pregunta (por ejemplo, `gemini-3.8-flash` para respuestas rápidas y `gemini-4-argon` para explicaciones largas).
- **RAG mejorado**: el equipo ha mejorado la búsqueda en el corpus respecto al `buscar_relevantes` básico (embeddings, reranking, búsqueda semántica, o cualquier otra mejora demostrable).
- **Evaluación propia**: el equipo incluye ejemplos de preguntas y respuestas en el writeup que demuestran la calidad de su tutor, con análisis de dónde funciona bien y dónde falla.

## Notas

- No se evalúa la cantidad de código sino su calidad y el resultado final.
- Un tutor simple que funciona bien puntúa más que uno complejo que falla.
- La originalidad de la idea cuenta, pero la ejecución cuenta más.
- Usar `request_type: "app"` en la demo final es obligatorio.
