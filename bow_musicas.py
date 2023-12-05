# Adicione as importações necessárias
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import preprocessamento as pre  # Altere o nome do arquivo conforme necessário

# Chame a função de scraping
pre.scrapping()

# Carrega o arquivo CSV
df = pd.read_csv('musicas.csv')

# Cria um corpus a partir das músicas marcadas com 's' na coluna 'incluir'
corpus = df[df['incluir'] == 's']['letra'].tolist()  # Transforma as letras em uma lista para o cálculo do TF-IDF

# Calcula as palavras importantes usando a função do módulo preprocessamento
important_words = pre.calculate_tfidf(corpus)

# Adiciona as palavras importantes ao DataFrame
df['important_words'] = important_words

# Crie um objeto WordCloud com as palavras importantes
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(" ".join(important_words))

# Exiba a nuvem de palavras
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()