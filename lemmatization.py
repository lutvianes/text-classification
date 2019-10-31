from spacy.lang.en import English
import spacy

# Load English tokenizer, tagger, parser, NER and word vectors
nlp = spacy.load("en_core_web_sm")


# Implementing lemmatization
lem = nlp("runs running runner ran")
# finding lemma for each word
for word in lem:
    print(word.text, word.lemma_)
