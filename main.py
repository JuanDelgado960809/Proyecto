import nltk

# 1. Configuración de NLTK: establecer ruta de datos antes de descargar paquetes
nltk.data.path.append(r'C:/Users/juan/AppData/Roaming/nltk_data')

# Paquetes necesarios
nltk.download('punkt')        # Tokenizadores de oraciones y palabras
nltk.download('stopwords')    # Listas de palabras vacías (stopwords)

# 2. Importaciones
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist

# 3. Texto de presentación del grupo
texto = (
    """
Somos campistas del programa Inteligencia Artificial nivel explorador basico, pertenecemos al grupo 10, el cual esta 
conformado por:
Mi Nombre es Juan David Delgado Macias actualmente laboro en una empresa distribuidora de productos farmaceuticos,
mi trabajo consiste en la elaboracion de propuestas para contratos de dispensacion, atencion de incidentes TIC,
mi pasatiempo favorito esta en viajar, compartir con mi familia y descansar.
Mi compañero es Carlos Eduardo Hernandez Piedrahita actualmente labora en una empresa de desarrollo de Software y 
lidera proyectos de desarrollo, su pasatiempo favorito es programar y compartir tiempo en familia.
La compañera Kathiuska Del Carmen Mangones Ramos actualmente se desempeña como analista de datos y su pasatiempo 
es leer, hacer deporte y compartir en familia.
Y el ultimo compañero Juan Carlos Quintero Salcedo es estudiante de ingeniera de sistemas, su pasatiempo favorito 
es programar, pasear y descanasar.
"""
)

# 4. Tokenización
oraciones = sent_tokenize(texto, language='spanish')
palabras = word_tokenize(texto, language='spanish')

# 5. Filtrado de stopwords y signos
stop_words = set(stopwords.words('spanish'))
palabras_filtradas = [w.lower() for w in palabras if w.isalpha() and w.lower() not in stop_words]

# 6. Análisis de frecuencia
frecuencia = FreqDist(palabras_filtradas)

# 7. Salidas
print("--- Párrafo de presentación ---\n")
print(texto)

print("\n--- Oraciones tokenizadas ---")
for i, oracion in enumerate(oraciones, 1):
    print(f"{i}: {oracion}")

print("\n--- 10 palabras más frecuentes ---")
for palabra, cuenta in frecuencia.most_common(10):
    print(f"{palabra}: {cuenta}")

# 8. Ejemplo de extracción de nombres (NER simple con regexp)
import re
nombres = re.findall(r"[A-Z][a-z]+(?:\s[A-Z][a-z]+){1,2}", texto)
print("\n--- Nombres detectados ---")
for nombre in set(nombres):
    print(nombre)

# Fin del script: este código genera un análisis básico de PLN sobre el texto de presentación.
