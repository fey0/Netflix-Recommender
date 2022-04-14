import pandas as pd 
import sys
from sklearn.feature_extraction.text import CountVectorizer
import string
from sklearn.feature_extraction.text import TfidfTransformer, TfidfVectorizer
from nltk.corpus import stopwords
from sklearn.metrics.pairwise import cosine_similarity


df = pd.read_csv("~/desktop/netflix_titles.csv")

df.drop(['director', 'cast', 'country', 'date_added', 'release_year', 'rating', 'duration'], axis=1, inplace=True)

#for line in df['description']: 
#	line = line.lower()


#tfidf = CountVectorizer(max_features=8000, stop_words='english')
tfidf = TfidfVectorizer(stop_words='english')
tfidf_x = tfidf.fit_transform(df['description'].str.lower())

cosim_df=pd.DataFrame(cosine_similarity(tfidf_x))

cosim_df.index=df.title
cosim_df.columns=df.title

get_rec=cosim_df.loc['Death Note'].sort_values(ascending = False)

print(get_rec)

