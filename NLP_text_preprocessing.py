import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('wordnet')
nltk.download('omw-1.4')

text="The Student were studying and playing football."

tokens= word_tokenize(text)

print(tokens)


# stemming
stemmer =PorterStemmer()

stems=[stemmer.stem(word) for word in tokens ]
print(stems)

# lemmatizer

lematizer= WordNetLemmatizer()

lemmas=[lematizer.lemmatize(word.lower(),pos='v')for word in tokens]

print("/nlemmatizer:")
print(lemmas)