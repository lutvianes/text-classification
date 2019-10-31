import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
from sklearn.base import TransformerMixin
from sklearn.pipeline import Pipeline

# Loading TSV file
df_amazon = pd.read_csv ("datasets/amazon_alexa.tsv", sep="\t")

print(df_amazon.head())
