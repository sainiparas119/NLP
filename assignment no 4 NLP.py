#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install spacy')
import spacy
nlp = spacy.load('en_core_web_sm')
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize, RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, LancasterStemmer, WordNetLemmatizer
import string


# In[2]:


# Download required resources
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')


# In[3]:


# Initialize objects
stop_words = set(stopwords.words("english"))
porter = PorterStemmer()
lancaster = LancasterStemmer()
lemmatizer = WordNetLemmatizer()
regex_tokenizer = RegexpTokenizer(r'\w+')


# In[4]:


# question-1:Tokenize a simple sentence using word_tokenize. ( "Natural Language Processing with Python is fun")
doc = nlp(u'natural langugae processing is fun with pyhton ')
for token in doc:
    print(token.text)


# In[5]:


# Question 2: Remove punctuation from a sentence
sentence= "Hello there! How's the weather today?"
tokens= word_tokenize(sentence)
no_punct= [word for word in tokens if word.isalnum()]
print(no_punct)


# In[6]:


# Question 3: Remove stopwords from a sentence
sentence3 = "This is a simple sentence for stopword removal."
tokens3 = word_tokenize(sentence3)
filtered3 = [word for word in tokens3 if word.lower() not in stop_words]
print( filtered3)


# In[7]:


# Question 4: Perform stemming using PorterStemmer
sentence4 = "The striped bats are hanging on their feet for best."
tokens4 = word_tokenize(sentence4)
stemmed4 = [porter.stem(word) for word in tokens4]
print(stemmed4)


# In[8]:


# Question 5: Perform lemmatization using WordNetLemmatizer
sentence5 = "The geese are flying south for the winter."
tokens5 = word_tokenize(sentence5)
lemmatized5 = [lemmatizer.lemmatize(word) for word in tokens5]
print(lemmatized5)


# In[9]:


# Question 6: Convert text to lowercase and remove punctuation
sentence6 = "Hello, World! NLP with Python."
lower6 = sentence6.lower()
no_punct6 = ''.join([char for char in lower6 if char not in string.punctuation])
print( no_punct6)


# In[10]:


# Question 7: Tokenize a sentence into sentences
sentence7 = "Hello World. This is NLTK. Let's explore NLP!"
sentences7 = sent_tokenize(sentence7)
print(sentences7)


# In[11]:


# Question 8: Stem words in a sentence using LancasterStemmer
sentence8 = "Loving the experience of learning NLTK"
tokens8 = word_tokenize(sentence8)
stemmed8 = [lancaster.stem(word) for word in tokens8]
print(stemmed8)


# In[12]:


# Question 9: Remove both stopwords and punctuation from a sentence
sentence9 = "This is a test sentence, with stopwords and punctuation!"
tokens9 = word_tokenize(sentence9)
filtered9 = [word for word in tokens9 if word.lower() not in stop_words and word.isalnum()]
print(filtered9)


# In[13]:


# Question 10: Lemmatize words with their part-of-speech (POS) tag
from nltk.corpus import wordnet

def get_wordnet_pos(word):
    """Map POS tag to first character for lemmatizer."""
    tag = nltk.pos_tag([word])[0][1][0].upper()
    tag_dict = {"J": wordnet.ADJ, "N": wordnet.NOUN, "V": wordnet.VERB, "R": wordnet.ADV}
    return tag_dict.get(tag, wordnet.NOUN)

sentence10 = "The striped bats are hanging on their feet."
tokens10 = word_tokenize(sentence10)
lemmatized10 = [lemmatizer.lemmatize(word, get_wordnet_pos(word)) for word in tokens10]
print(lemmatized10)


# In[14]:


# Question 11: Tokenize and remove stopwords, punctuation, and perform stemming
sentence11 = "Running through the forest, the fox is faster."
tokens11 = word_tokenize(sentence11)
filtered11 = [porter.stem(word) for word in tokens11 if word.lower() not in stop_words and word.isalnum()]
print(filtered11)


# In[15]:


#Question 12: Count stopwords in a sentence
sentence12 = "This is an example sentence for counting stopwords."
tokens12 = word_tokenize(sentence12)
stopword_count12 = len([word for word in tokens12 if word.lower() in stop_words])
print(stopword_count12)


# In[16]:


# Question 13: Perform stemming and remove punctuation using RegexTokenizer
sentence13 = "Stemming, punctuation! Removal example."
tokens13 = regex_tokenizer.tokenize(sentence13)
stemmed13 = [porter.stem(word) for word in tokens13]
print( stemmed13)


# In[17]:


# Question14: Remove punctuation using regex and NLTK
sentence14 = "Punctuation removal with regex in NLP!"
tokens14 = regex_tokenizer.tokenize(sentence14)
print(tokens14)


# In[18]:


# Question 15: Tokenize text into words, remove stopwords, and lemmatize
sentence15 = "The dogs are barking loudly."
tokens15 = word_tokenize(sentence15)
filtered15 = [lemmatizer.lemmatize(word) for word in tokens15 if word.lower() not in stop_words and word.isalnum()]
print(filtered15)


# In[ ]:




