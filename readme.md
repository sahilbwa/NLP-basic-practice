# NLP Text Preprocessing: Tokenization, Stemming, and Lemmatization

## 📌 Project Overview

This project demonstrates three important techniques used in **Natural Language Processing (NLP)**:

1. **Tokenization**
2. **Stemming**
3. **Lemmatization**

These techniques are commonly used to preprocess and normalize text before applying NLP tasks such as text classification, sentiment analysis, spam detection, and machine learning.

---

## 🛠️ Technologies Used

* Python
* NLTK (Natural Language Toolkit)

### Required Python Library

```bash
pip install nltk
```

---

## 📂 Project Structure

```text
NLP/
│
├── NLP_text_preprocessing.py
└── README.md
```

---

## 📦 NLTK Dataset Downloads

The project uses the following NLTK resources:

```python
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('wordnet')
nltk.download('omw-1.4')
```

### Explanation

* **punkt** – Used for tokenization.
* **punkt_tab** – Required by newer versions of NLTK for sentence and word tokenization.
* **wordnet** – Used by the WordNet Lemmatizer.
* **omw-1.4** – Provides additional linguistic data used by WordNet.

---

# 1. Tokenization

## What is Tokenization?

**Tokenization** is the process of breaking a sentence or paragraph into smaller units called **tokens**.

Tokens can be:

* Words
* Punctuation marks
* Sentences

For example:

```text
The Student were studying and playing football.
```

After tokenization:

```text
['The', 'Student', 'were', 'studying', 'and', 'playing', 'football', '.']
```

### Python Code

```python
from nltk.tokenize import word_tokenize

tokens = word_tokenize(text)

print(tokens)
```

### Why is Tokenization Important?

Tokenization is usually one of the first steps in NLP preprocessing. It converts raw text into smaller units that can be processed by NLP algorithms.

---

# 2. Stemming

## What is Stemming?

**Stemming** is the process of reducing words to their basic **stem** by removing prefixes or suffixes.

Stemming does not always produce a proper English word. It uses a rule-based approach to reduce words.

For example:

```text
studying → studi
playing  → play
```

### Python Code

```python
from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

stems = [stemmer.stem(word) for word in tokens]

print(stems)
```

### Example Output

```text
['the', 'student', 'were', 'studi', 'and', 'play', 'football', '.']
```

### Advantages of Stemming

* Fast
* Simple to implement
* Useful when exact grammatical words are not important
* Reduces different word forms to a common stem

### Disadvantages of Stemming

* May produce words that are not valid English words
* Can sometimes remove too much or too little from a word
* Less linguistically accurate than lemmatization

---

# 3. Lemmatization

## What is Lemmatization?

**Lemmatization** reduces a word to its **base or dictionary form**, known as a **lemma**.

Unlike stemming, lemmatization considers the meaning and grammatical role of the word.

For example:

```text
studying → study
playing  → play
were     → be
```

### Python Code

```python
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

lemmas = [
    lemmatizer.lemmatize(word.lower(), pos='v')
    for word in tokens
]

print("\nLemmatizer:")
print(lemmas)
```

The parameter:

```python
pos='v'
```

tells the lemmatizer to treat the words as **verbs**.

### Example Output

```text
['the', 'student', 'be', 'study', 'and', 'play', 'football', '.']
```

### Advantages of Lemmatization

* Produces meaningful dictionary words
* More linguistically accurate
* Considers the grammatical form of words
* Better for applications where word meaning is important

### Disadvantages of Lemmatization

* Slower than stemming
* Requires more linguistic resources
* Requires the correct Part-of-Speech (POS) tag for accurate results

---

# 🔍 Stemming vs Lemmatization

| Feature              | Stemming         | Lemmatization                      |
| -------------------- | ---------------- | ---------------------------------- |
| Method               | Rule-based       | Dictionary and linguistic analysis |
| Output               | Stem             | Dictionary/base word               |
| Speed                | Faster           | Slower                             |
| Accuracy             | Lower            | Higher                             |
| Produces valid words | Not always       | Usually                            |
| Example              | studying → studi | studying → study                   |
| Example              | were → were      | were → be                          |

---

# 🔄 Complete NLP Preprocessing Flow

The basic flow demonstrated in this project is:

```text
Raw Text
    │
    ▼
Tokenization
    │
    ▼
Individual Tokens
    │
    ├───────────────┐
    ▼               ▼
Stemming      Lemmatization
    │               │
    ▼               ▼
Stem Words     Base Words
```

For example:

```text
Input:
The Student were studying and playing football.

        │
        ▼

Tokenization:
The | Student | were | studying | and | playing | football

        │
        ├──────────────────┐
        ▼                  ▼

Stemming             Lemmatization
studying → studi     studying → study
playing → play       playing → play
                     were → be
```

---

# 🚀 Complete Code

```python
import nltk

from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer

# Download required NLTK resources
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('wordnet')
nltk.download('omw-1.4')

# Input text
text = "The Student were studying and playing football."

# -------------------------
# 1. Tokenization
# -------------------------

tokens = word_tokenize(text)

print("Tokens:")
print(tokens)


# -------------------------
# 2. Stemming
# -------------------------

stemmer = PorterStemmer()

stems = [stemmer.stem(word) for word in tokens]

print("\nStemming:")
print(stems)


# -------------------------
# 3. Lemmatization
# -------------------------

lemmatizer = WordNetLemmatizer()

lemmas = [
    lemmatizer.lemmatize(word.lower(), pos='v')
    for word in tokens
]

print("\nLemmatization:")
print(lemmas)
```

---

## 🎯 Learning Outcomes

After completing this project, you will understand:

* What NLP text preprocessing is
* How tokenization works
* How to split text into individual tokens
* How stemming reduces words to their stems
* How lemmatization converts words to their base forms
* The difference between stemming and lemmatization
* How to use NLTK for basic NLP preprocessing

---

## 📚 Real-World Applications

These preprocessing techniques are commonly used in:

* Sentiment Analysis
* Text Classification
* Spam Detection
* Search Engines
* Chatbots
* Question Answering Systems
* Document Classification
* Text Summarization
* Natural Language Understanding

---

## ⚠️ Note

Stemming and lemmatization can produce different results depending on the algorithm and the **Part-of-Speech (POS)** provided.

For example, in this project:

```python
pos='v'
```

means that words are treated as **verbs**.

Using a different POS such as:

```python
pos='n'
```

for nouns may produce different lemmatization results.

---

## 👨‍💻 Author

**Sahil**

This project was created as part of learning **Natural Language Processing (NLP) and Text Preprocessing using Python and NLTK**.
