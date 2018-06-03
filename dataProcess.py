import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from wordcloud import WordCloud, STOPWORDS
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import os
from PIL import Image

currdir = os.path.dirname(__file__)

def data_process(messages, k=2):
    vectorizer = TfidfVectorizer(min_df=1)
    x = vectorizer.fit_transform(messages)
    model = KMeans(n_clusters=k, random_state=0, n_jobs=-2)
    model.fit(x)
    y = model.predict(x)
    return y


def get_text_from_clusters(corpus, y):
    text_arr = []
    for idx, cluster in enumerate(y):
        try:
            text_arr[cluster] += corpus[idx] + " "
            print()
        except IndexError:
            text_arr.insert(cluster, corpus[idx] + " ")
    return text_arr


def build_word_cloud(text_arr, img_name):
    fig = plt.figure()
    mask = np.array(Image.open(os.path.join(currdir, "cloud.png")))
    for i in range(0, len(text_arr)):
        wordcloud = WordCloud(background_color='white',
                              mask=mask,
                              width=1200,
                              height=1000
                              ).generate(text_arr[i])
        # fig.add_subplot(1, 2, i + 1)
        plt.imshow(wordcloud)
        plt.axis('off')
    plt.savefig(img_name)
    plt.show(block=True)
