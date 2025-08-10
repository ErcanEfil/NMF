import pandas as pd
from sklearn.decomposition import NMF
from sklearn.feature_extraction.text import TfidfVectorizer


df = pd.read_excel(r"C:\Users\User\Desktop\MachineLearning\NMF\news.xls")

#On Hazirlik

df.isna().sum()
df.drop_duplicates(subset=['content'], inplace=True)

stop_words = ['ve','ile','ama','fakat','ancak','daha','çok','gibi','ise','de','da','mi','mu','mü',
                'bir','bu','şu','o','olarak','çünkü','hem','hemde','ki','ya','ya da','ise','en','çok','için',
                'kadar','üzerine','göre','sadece','tüm','ın','un','ün','nın','in','nin','ye','nde']

samples = df['content'].astype(str).str.replace(r'\n', ' ', regex=True).str.strip()

vectorizer = TfidfVectorizer(max_df=0.95,min_df=2, ngram_range=(1, 2), stop_words=stop_words)

X = vectorizer.fit_transform(samples)

model = NMF(n_components=10, random_state=42,max_iter=500)
W = model.fit_transform(X)
H = model.components_

feature_names = vectorizer.get_feature_names_out()
topn = 10
for k, comp in enumerate(H):
    top_terms = [feature_names[i] for i in comp.argsort()[:-topn-1:-1]]
    print(f"Topic {k}: {' | '.join(top_terms)}")


## similarity

from sklearn.preprocessing import normalize

norm_features = normalize(W)

df = pd.DataFrame(norm_features, index=df['content'])

current_topic = df.iloc[0]  

similarity = df.dot(current_topic)

print(similarity.nlargest())

