#importar la libreria nltk
import nltk

#desde nltk descargar el paquete stopwords
from nltk.corpus import stopwords
nltk.download('stopwords')

lista_stopwords = stopwords.words('english')

#imprimir la lista de stopwords
print(lista_stopwords)

