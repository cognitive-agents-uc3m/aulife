# Ideas de proyecto

Aquí tienes varias ideas para tu tutor virtual. Puedes elegir una tal cual, combinar varias o inventar la tuya propia. Lo importante es que funcione bien y demuestre un uso creativo de la API.

---

## 1. Tutor de historia de la IA

Usa los documentos del corpus sobre la historia de la inteligencia artificial para crear un tutor que pueda responder preguntas, explicar conceptos clave y situar los hitos en su contexto histórico.

**Dificultad:** Básico

**Pistas de implementación:**
- Carga todo el corpus de `corpus/` con `cargar_documentos.py` y mejora la función de búsqueda para que encuentre fragmentos más relevantes.
- Añade al prompt del sistema instrucciones para que el tutor cite fuentes cuando responda.
- Implementa un modo "línea del tiempo" donde el tutor guíe al estudiante cronológicamente por los avances de la IA.

---

## 2. Tutor de matemáticas paso a paso

Un tutor que resuelve problemas de matemáticas desglosando cada paso y explicando el razonamiento detrás. El estudiante puede pedir que repita un paso con más detalle o que lo explique de otra forma.

**Dificultad:** Intermedio

**Pistas de implementación:**
- Usa un prompt del sistema que fuerce al modelo a responder siempre con pasos numerados y justificación de cada operación.
- Implementa un mecanismo donde el estudiante pueda decir "no entiendo el paso 3" y el tutor amplíe solo ese paso.
- Usa `gemini-4-argon` para las resoluciones porque razona mejor en matemáticas.

---

## 3. Tutor multimodal de diagramas

Un tutor capaz de analizar imágenes de diagramas, gráficos o esquemas y explicar lo que muestran. El estudiante sube una foto de sus apuntes o de un diagrama del libro y el tutor lo interpreta.

**Dificultad:** Intermedio

**Pistas de implementación:**
- Usa las funciones de `multimodal.py` para enviar imágenes junto con la pregunta del estudiante.
- Configura el prompt para que el tutor describa primero lo que ve en la imagen antes de responder la pregunta.
- Prueba con las imágenes de ejemplo en `corpus/imagenes/` (perceptron, transformer, CNN).

---

## 4. Generador de exámenes tipo test

Un asistente de estudio que lee el corpus y genera preguntas de opción múltiple sobre el contenido. Después de que el estudiante responda, le dice si acertó y le explica por qué.

**Dificultad:** Intermedio

**Pistas de implementación:**
- Pide al modelo que genere las preguntas en un formato estructurado (por ejemplo, JSON) para poder parsear las opciones y la respuesta correcta.
- Implementa un bucle de estudio: pregunta, respuesta del estudiante, corrección, explicación, siguiente pregunta.
- Lleva la cuenta de aciertos y errores para dar un resumen al final de la sesión.

---

## 5. Tutor de idiomas con corrección gramatical

Un tutor de idiomas (inglés, francés, alemán...) que mantiene una conversación con el estudiante y le corrige los errores gramaticales de forma constructiva, explicando la regla que aplica.

**Dificultad:** Intermedio

**Pistas de implementación:**
- Configura el prompt para que el tutor responda siempre en dos bloques: primero la corrección (si la hay) y luego la respuesta natural a la conversación.
- Añade un sistema de niveles donde el tutor se adapta al vocabulario del estudiante según sus errores.
- Usa el historial de conversación para detectar errores recurrentes y hacer hincapié en ellos.

---

## 6. Revisor de código

Un tutor de programación que revisa fragmentos de código del estudiante, detecta errores, sugiere mejoras y explica buenas prácticas. Enfocado en Python para principiantes.

**Dificultad:** Avanzado

**Pistas de implementación:**
- Usa `gemini-4-argon` que tiene buen rendimiento en tareas de código.
- Configura el prompt para que el tutor no dé la solución directamente sino que haga preguntas que guíen al estudiante hacia el error.
- Añade al corpus documentos con patrones comunes de errores en Python para que el tutor los reconozca.

---

## 7. Tutor adaptativo multinivel

Un tutor que detecta el nivel del estudiante a partir de sus preguntas y respuestas, y ajusta automáticamente la complejidad de sus explicaciones. Empieza con explicaciones simples y va profundizando según el estudiante demuestre comprensión.

**Dificultad:** Avanzado

**Pistas de implementación:**
- Mantiene un "perfil" del estudiante en memoria (variable en el código) que actualiza tras cada interacción: temas dominados, temas pendientes, nivel estimado.
- Inyecta ese perfil en el prompt del sistema antes de cada petición para que el modelo ajuste su respuesta.
- Usa dos modelos: `gemini-3.8-flash` para clasificar el nivel del estudiante y `gemini-4-argon` para generar la respuesta adaptada.

---

## 8. Tutor de debate y pensamiento crítico

Un tutor que presenta un tema controvertido de la IA (sesgo algorítmico, automatización del empleo, privacidad) y guía al estudiante en un debate estructurado, presentando argumentos de ambos lados y pidiendo que defienda una postura.

**Dificultad:** Avanzado

**Pistas de implementación:**
- Carga los documentos sobre ética de la IA del corpus como contexto para los debates.
- Implementa un formato de debate por turnos: el tutor presenta el tema, el estudiante elige postura, el tutor argumenta en contra, el estudiante responde.
- Al final del debate, el tutor evalúa la solidez de los argumentos del estudiante y sugiere puntos que no consideró.
