"""
cargar_documentos.py -- Ejemplo de carga de corpus multiformato.

Uso:
    from cargar_documentos import cargar_corpus, buscar_relevantes

Este módulo muestra cómo:
1. Leer archivos de texto y PDF de una carpeta.
2. Buscar los fragmentos más relevantes para una pregunta.

NOTA: La búsqueda es por coincidencia de palabras (deliberadamente básica).
      Un buen proyecto mejoraría esto con embeddings o TF-IDF.
      Los formatos soportados aquí son solo un punto de partida;
      los equipos pueden ampliar la carga a HTML, vídeos, etc.
"""

import os


def extraer_texto(ruta: str) -> str | None:
    """
    Extrae texto de un archivo según su extensión.
    Soporta .txt y .md de forma nativa.
    Para .pdf, intenta usar PyPDF2 si está instalado.
    """
    nombre = ruta.lower()

    if nombre.endswith((".txt", ".md")):
        with open(ruta, "r", encoding="utf-8") as f:
            return f.read()

    if nombre.endswith(".pdf"):
        try:
            from PyPDF2 import PdfReader
            reader = PdfReader(ruta)
            texto = ""
            for pagina in reader.pages:
                contenido = pagina.extract_text()
                if contenido:
                    texto += contenido + "\n"
            return texto
        except ImportError:
            print(f"  Aviso: para leer '{os.path.basename(ruta)}', instala PyPDF2 (pip install PyPDF2)")
            return None

    # Formato no reconocido: saltar
    return None


def cargar_corpus(directorio: str = "corpus") -> list[dict]:
    """
    Carga todos los documentos de texto y PDF del corpus.

    Devuelve una lista de diccionarios con:
    - titulo: nombre del archivo
    - archivo: ruta al archivo
    - texto: contenido extraído
    """
    documentos = []

    for archivo in sorted(os.listdir(directorio)):
        ruta = os.path.join(directorio, archivo)
        if not os.path.isfile(ruta):
            continue

        texto = extraer_texto(ruta)
        if texto:
            documentos.append({
                "titulo": archivo,
                "archivo": archivo,
                "texto": texto,
            })
            print(f"  Cargado: {archivo} ({len(texto)} caracteres)")

    print(f"\nTotal: {len(documentos)} documentos cargados.")
    return documentos


def fragmentar(texto: str, tamano: int = 1000, solapamiento: int = 200) -> list[str]:
    """
    Divide un texto largo en fragmentos con solapamiento.

    Args:
        texto: texto completo
        tamano: caracteres por fragmento
        solapamiento: caracteres que se repiten entre fragmentos consecutivos

    Devuelve una lista de fragmentos.
    """
    fragmentos = []
    inicio = 0
    while inicio < len(texto):
        fin = inicio + tamano
        fragmentos.append(texto[inicio:fin])
        inicio += tamano - solapamiento
    return fragmentos


def buscar_relevantes(
    pregunta: str,
    documentos: list[dict],
    max_fragmentos: int = 3,
    tamano_fragmento: int = 1500,
) -> str:
    """
    Búsqueda simple: encuentra los fragmentos del corpus más relevantes
    para una pregunta dada.

    ESTA FUNCIÓN ES DELIBERADAMENTE BÁSICA. Usa coincidencia de palabras.
    Ideas para mejorarla:
    - Usar embeddings (text-embedding de Gemini o sentence-transformers)
    - Implementar TF-IDF con scikit-learn
    - Usar una base de datos vectorial (ChromaDB, FAISS)

    Args:
        pregunta: la pregunta del usuario
        documentos: lista devuelta por cargar_corpus()
        max_fragmentos: número máximo de fragmentos a devolver
        tamano_fragmento: tamaño de cada fragmento en caracteres
    """
    palabras = set(pregunta.lower().split())

    # Puntuar cada fragmento de cada documento
    candidatos = []
    for doc in documentos:
        for frag in fragmentar(doc["texto"], tamano=tamano_fragmento):
            frag_lower = frag.lower()
            puntuacion = sum(1 for p in palabras if p in frag_lower)
            if puntuacion > 0:
                candidatos.append((puntuacion, doc["titulo"], frag))

    # Ordenar por puntuación descendente y tomar los mejores
    candidatos.sort(key=lambda x: x[0], reverse=True)
    mejores = candidatos[:max_fragmentos]

    if not mejores:
        return "(No se encontraron fragmentos relevantes en el corpus.)"

    contexto = ""
    for puntuacion, titulo, frag in mejores:
        contexto += f"\n--- Fuente: {titulo} ---\n{frag}\n"

    return contexto
