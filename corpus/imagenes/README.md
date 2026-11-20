# Imagenes educativas

Este directorio contiene diagramas e ilustraciones educativas sobre inteligencia artificial que el tutor puede referenciar y que los participantes pueden usar para enriquecer sus proyectos.

## Imagenes sugeridas

Los participantes pueden anadir aqui imagenes educativas relevantes para su tutor. Algunas sugerencias:

- **Diagrama del perceptron**: esquema que muestre entradas, pesos, suma ponderada, funcion de activacion y salida.
- **Arquitectura Transformer**: diagrama de bloques mostrando encoder, decoder, mecanismo de autoatencion y feed-forward.
- **Capas de una CNN**: visualizacion de como los filtros convolucionales detectan patrones progresivamente mas abstractos (bordes, texturas, formas, objetos).
- **Pipeline de RAG**: diagrama de flujo que ilustre el proceso de busqueda en el corpus y generacion de respuesta con contexto.

## Formato

Se recomienda usar imagenes en formato PNG o JPG con resolucion suficiente para ser legibles. Para el analisis multimodal con el modelo, las imagenes deben pesar menos de 5 MB.

## Uso en el tutor

El codigo de `multimodal.py` permite enviar imagenes al modelo para que las analice. Los participantes pueden usar esta funcionalidad para crear un tutor que explique diagramas o que pida a los estudiantes interpretar visualizaciones.
