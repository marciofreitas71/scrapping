from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
from nltk.corpus import stopwords
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd
import proprocessamento as pre


pre.scrapping()

# Carrega o arquivo CSV
df = pd.read_csv('musicas.csv')

# Cria um corpus a partir das músicas marcadas com 's' na coluna 'incluir'
corpus = ' '.join(df[df['incluir'] == 's']['letra'])

# Crie um objeto WordCloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(pre.preprocess_text(corpus))

# Exiba a nuvem de palavras
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()

