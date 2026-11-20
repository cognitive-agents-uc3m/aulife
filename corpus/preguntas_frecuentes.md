# Preguntas Frecuentes sobre Inteligencia Artificial

## Que es la inteligencia artificial?

La inteligencia artificial es un campo de la informatica que busca crear sistemas capaces de realizar tareas que normalmente requieren inteligencia humana: comprender lenguaje, reconocer imagenes, tomar decisiones, aprender de la experiencia. No existe una definicion unica y universalmente aceptada; el termino abarca desde simples reglas if-then hasta modelos con miles de millones de parametros.

## Cual es la diferencia entre IA, aprendizaje automatico y aprendizaje profundo?

Son conceptos anidados. La IA es el campo mas amplio: cualquier sistema que exhibe comportamiento inteligente. El aprendizaje automatico (machine learning) es un subcampo de la IA donde los sistemas aprenden de datos en lugar de ser programados explicitamente. El aprendizaje profundo (deep learning) es un subcampo del aprendizaje automatico que usa redes neuronales con muchas capas. No todo machine learning es deep learning, y no toda IA usa machine learning.

## Como funciona un modelo de lenguaje grande (LLM)?

Un LLM es una red neuronal (generalmente basada en la arquitectura Transformer) entrenada para predecir la siguiente palabra en una secuencia de texto. Se entrena con cantidades masivas de texto de internet, libros y otros documentos. Durante el entrenamiento, ajusta miles de millones de parametros para capturar patrones estadisticos del lenguaje. Al generar texto, el modelo predice palabra por palabra (en realidad, token por token) cual es la continuacion mas probable del texto que lleva escrito.

## Que es un Transformer?

El Transformer es una arquitectura de red neuronal presentada en 2017 en el articulo "Attention Is All You Need". Su innovacion principal es el mecanismo de atencion, que permite a cada parte del texto "atender" a cualquier otra parte, capturando relaciones a larga distancia. A diferencia de las redes recurrentes, procesa toda la secuencia en paralelo, lo que acelera enormemente el entrenamiento. Es la base de practicamente todos los modelos de lenguaje modernos (GPT, BERT, Gemini, Claude, LLaMA).

## Que es el prompt engineering?

Es la practica de disenar y refinar las instrucciones (prompts) que se dan a un modelo de lenguaje para obtener mejores resultados. Un buen prompt proporciona contexto, especifica el formato deseado, incluye ejemplos si es necesario y establece restricciones claras. No es una ciencia exacta: requiere experimentacion y comprension de como el modelo interpreta las instrucciones.

## Puede la IA ser creativa?

Depende de como definamos creatividad. Los modelos de IA generativa pueden producir imagenes, musica, textos y codigo que nunca existieron antes, combinando patrones aprendidos de formas novedosas. Sin embargo, no tienen intencionalidad, experiencia subjetiva ni motivacion propia. Su "creatividad" es fundamentalmente combinatoria: reorganizan y mezclan patrones de sus datos de entrenamiento. Si eso cuenta como creatividad genuina es una cuestion filosofica abierta.

## La IA va a sustituir a los profesores?

Es muy improbable que la IA sustituya completamente a los profesores. La educacion implica mucho mas que transmitir informacion: incluye motivacion, mentoria, desarrollo socioemocional, pensamiento critico y adaptacion al contexto cultural y personal de cada estudiante. Lo que si es probable es que la IA transforme el rol del profesor, automatizando tareas repetitivas (correccion, seguimiento) y permitiendo dedicar mas tiempo a las actividades de mayor valor pedagogico.

## Que es una alucinacion en IA?

Una alucinacion es cuando un modelo de lenguaje genera informacion que parece plausible y se presenta con seguridad, pero es factualmente incorrecta o completamente inventada. Los modelos de lenguaje no "saben" cosas en el sentido humano; predicen secuencias de texto probables. A veces, la continuacion mas probable estadisticamente no es la correcta. Por eso es fundamental verificar siempre la informacion que proporciona un LLM, especialmente en contextos donde la precision es critica.

## Que es RAG (Retrieval-Augmented Generation)?

RAG es una tecnica que combina un modelo de lenguaje con una base de conocimiento externa. En lugar de depender solo de lo que el modelo "recuerda" de su entrenamiento, el sistema primero busca informacion relevante en documentos y luego la proporciona al modelo como contexto para generar su respuesta. Esto reduce las alucinaciones y permite que el modelo trabaje con informacion actualizada o especifica de un dominio. El tutor que construireis en este taller usa una version basica de RAG.

## Que significa que un modelo tenga X mil millones de parametros?

Los parametros son los valores numericos internos del modelo (pesos de las conexiones entre neuronas) que se ajustan durante el entrenamiento. Un modelo con mas parametros tiene mayor capacidad para capturar patrones complejos, pero tambien requiere mas datos, mas tiempo de entrenamiento y mas memoria para ejecutarse. GPT-3 tiene 175 mil millones de parametros; modelos mas recientes pueden superar el billon. Mas parametros no garantizan mejor rendimiento: la calidad de los datos y el entrenamiento importan tanto o mas.

## Que es el fine-tuning?

El fine-tuning (ajuste fino) consiste en tomar un modelo preentrenado (que ya ha aprendido patrones generales del lenguaje) y entrenarlo adicionalmente con datos especificos de una tarea o dominio. Por ejemplo, un modelo general se puede ajustar con conversaciones medicas para crear un asistente sanitario. Es mucho mas eficiente que entrenar un modelo desde cero, ya que aprovecha el conocimiento general previamente adquirido.

## Que es un embedding?

Un embedding es una representacion numerica de un dato (palabra, frase, imagen) como un vector en un espacio de muchas dimensiones. La propiedad clave es que elementos semanticamente similares tienen embeddings cercanos en ese espacio. Por ejemplo, los embeddings de "gato" y "felino" estaran mas cerca entre si que los de "gato" y "avion". Los embeddings permiten a los modelos trabajar con significados de forma matematica.

## Es seguro compartir informacion personal con un chatbot de IA?

Depende del chatbot y de como esta configurado. En general, se recomienda no compartir informacion sensible (contrasenas, datos financieros, informacion medica detallada, numeros de identificacion) con chatbots publicos. Los datos que introduces pueden usarse para mejorar el modelo, almacenarse en servidores de terceros o ser accesibles a otros empleados de la empresa que proporciona el servicio. En un contexto controlado, como el de este taller con un proxy propio, los datos se gestionan internamente.

## Que diferencia hay entre IA estrecha e IA general?

La IA estrecha (narrow AI o weak AI) es la que existe actualmente: sistemas disenados para tareas especificas (reconocimiento facial, traduccion, jugar al ajedrez). Son muy buenos en lo suyo pero no pueden generalizar a tareas diferentes. La IA general (AGI, Artificial General Intelligence) seria un sistema con capacidades cognitivas comparables a las de un humano, capaz de aprender cualquier tarea intelectual. La AGI es un objetivo de investigacion, no una realidad actual, y hay un debate significativo sobre si y cuando se alcanzara.

## Como puedo saber si un texto ha sido generado por IA?

No existe un metodo fiable al 100%. Los detectores de texto generado por IA analizan patrones estadisticos (perplejidad, distribucion de tokens) pero tienen tasas significativas de falsos positivos y falsos negativos. Un texto editado por un humano tras ser generado por IA es particularmente dificil de detectar. Las herramientas de deteccion pueden ser utiles como indicador, pero no como prueba definitiva. La transparencia (declarar cuando se ha usado IA) es mas fiable que la deteccion automatica.

## Que impacto ambiental tiene la IA?

El entrenamiento de modelos grandes consume cantidades significativas de energia electrica y agua (para la refrigeracion de centros de datos). Entrenar un modelo como GPT-3 se estimo en cientos de toneladas de CO2 equivalente. Sin embargo, una vez entrenado, la inferencia (usar el modelo) es mucho mas eficiente. El impacto ambiental depende tambien de la fuente de energia de los centros de datos. Es un area de investigacion activa: se buscan modelos mas eficientes, hardware especializado con menor consumo y centros de datos alimentados por energia renovable.
