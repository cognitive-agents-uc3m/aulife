# Aulife -- Taller de Tutores Virtuales con IA

Semana de la Ciencia y de la Innovación de Madrid 2026 | Universidad Carlos III de Madrid

Cuatro equipos de universitarios tienen tres horas para construir un tutor virtual multimodal: un asistente educativo capaz de ver imágenes, leer documentos, escuchar preguntas por voz y responder de forma natural, fundamentado en el material de una asignatura.

## Inicio rápido

```bash
git clone https://github.com/cognitive-agents-uc3m/aulife
cd aulife
```

### Verificar conexión con el proxy

```bash
export PROXY_URL=https://tu-proxy.run.app
export API_KEY=sk-tu-clave
python starter_code/verificar_setup.py
```

### Ejecutar el tutor de ejemplo

```bash
pip install -r starter_code/requirements.txt
python starter_code/tutor.py
```

## Estructura del repositorio

```
starter_code/          Ejemplos de referencia en Python
  verificar_setup.py   Comprueba la conexión con el proxy
  ejemplo_chat_basico.py  Llamada mínima al modelo
  ejemplo_imagen.py    Enviar una imagen al modelo
  ejemplo_voz.py       Grabar audio y enviarlo al modelo
  multimodal.py        Llamada multimodal (imagen + texto)
  tutor.py             Tutor conversacional con corpus
  cargar_documentos.py Carga y búsqueda en el corpus
  requirements.txt     Dependencias de Python
  .env.ejemplo         Plantilla del archivo .env
corpus/                Material de ejemplo sobre IA
  imagenes/            Diagramas y figuras
docs/                  Documentación para participantes
  cheatsheet.txt       Referencia rápida de comandos y API
writeup_plantilla.md   Plantilla para el write-up del equipo
```

## El reto

Construir un tutor virtual multimodal y agnóstico al dominio que, alimentado con el material de cualquier asignatura, sea capaz de:

- Comprender preguntas en texto y en voz.
- Analizar imágenes: interpretar diagramas, fórmulas o fotografías de apuntes.
- Responder de forma natural, adaptada al nivel del estudiante y fundamentada en el material.
- Citar las fuentes: cada respuesta indica de qué documento se ha extraído la información.

## Proxy y modelos

El proxy LiteLLM es compatible con el SDK de OpenAI. Cada petición debe incluir `metadata.request_type` (`"dev"` para pruebas, `"app"` para la aplicación final).

```python
from openai import OpenAI

client = OpenAI(base_url=f"{PROXY_URL}/v1", api_key=API_KEY)
resp = client.chat.completions.create(
    model="gemini-3.8-flash",
    messages=[{"role": "user", "content": "Hola"}],
    extra_body={"metadata": {"request_type": "dev"}},
)
print(resp.choices[0].message.content)
```

Para ver los modelos disponibles:

```bash
curl $PROXY_URL/v1/models -H "Authorization: Bearer $API_KEY"
```

## Entregables

Cada equipo entrega:

1. **Código**: repositorio Git con el código funcional del tutor.
2. **Instrucciones de despliegue**: cómo poner en marcha la aplicación (`README.md` o `DEPLOY.md`).
3. **Write-up** (`writeup_plantilla.md`): enfoque, decisiones técnicas, resultados y lecciones aprendidas.

## Criterios de evaluación

| Criterio | Peso |
|----------|------|
| Write-up | 40% |
| Calidad de las respuestas | 20% |
| Capacidad multimodal | 20% |
| Demo en vivo | 20% |

## Licencia

MIT. Ver [LICENSE](LICENSE).
