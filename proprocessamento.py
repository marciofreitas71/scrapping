from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import string
import nltk
from nltk.corpus import stopwords
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd
from tqdm import tqdm
import os

nltk.download('stopwords')
stop_words = set(stopwords.words('portuguese'))

def preprocess_text(text):
    text = text.strip()
    text = text.lower().replace('pra', '')
    text = ''.join([char for char in text if char not in string.punctuation])
    words = text.split()
    words = [word for word in words if word not in stop_words]
    text = ' '.join(words)
    return text


def scrapping():
    # Scraping das músicas
    html = urlopen('https://www.letras.mus.br/caetano-veloso/')
    url_base = 'https://www.letras.mus.br'
    bs = BeautifulSoup(html.read(), 'html.parser')

    lista_musicas = bs.findAll('a', {'class': 'songList-table-songName'})

    # Inicializa um DataFrame para armazenar as músicas
    data = {'titulo': [], 'letra': [], 'incluir': []}

    for musica in tqdm(lista_musicas, desc= "Adicionando as músicas"):
        if 'href' in musica.attrs:
            link = musica.attrs['href']
            text = musica.get_text(strip=True)
            
            if text:
                # Acessa a página vinculada ao link da música
                musica_html = urlopen(url_base + link)
                musica_bs = BeautifulSoup(musica_html.read(), 'html.parser')

                # Localiza o elemento HTML que contém o texto da música (ajuste conforme necessário)
                musicas = musica_bs.find('div', {'class': 'lyric-original'})

                musica_str = str(musicas)
                musica_final = musica_str.replace('<br/>', ' ').replace('<p>', ' ').replace('</p>', ' ').replace('<div class="lyric-original">', ' ').replace('</div>', ' ')
                
                data['titulo'].append(text)
                data['letra'].append(musica_final)
                data['incluir'].append('s')
                print(f'Adicionada a música: {text}')
                os.system('cls')


    # Cria um DataFrame a partir dos dados das músicas
    df = pd.DataFrame(data)

    # Salva o DataFrame em um arquivo CSV
    df.to_csv('musicas.csv', index=False)
    print(f"O DataFrame foi salvo no arquivo 'musicas.csv'")