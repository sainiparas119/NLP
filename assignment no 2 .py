#!/usr/bin/env python
# coding: utf-8

# In[1]:


import spacy


# In[2]:


nlp = spacy.load('en_core_web_sm')


# In[3]:


with open("owlcreek.txt", "r") as file:
    text = file.read()


# # Quesion : 1

# In[16]:


#Create a Doc object from the file owlcreek.txt
doc = nlp(text)
doc


# # Question : 2

# In[15]:


# How many tokens are contained in the file?
for t in doc:
    print(t)


# # Question 3

# In[23]:


#How many sentences are contained in the file?
sent = list(doc.sents)
print(f"len of sentences: {len(sent)}")


# # Question 4

# In[24]:


#Print the second sentence in the document
sent[1]


# # Question 5

# In[25]:


#For each token in the sentence above, print its text, POS tag, dep tag and lemma.
for token in doc:
    print(f"Token: {token.text}, POS: {token.pos_}, Dep: {token.dep_}, Lemma: {token.lemma_}")


# # Question 6

# In[26]:


# Write a matcher called 'Swimming' that finds both occurrences of the phrase "swimming vigorously" in the text.
with open("owlcreek.txt", 'r') as file:
    text = file.read()
    print(text)


# In[17]:


import spacy 
nlp = spacy.load('en_core_web_sm')

from spacy.matcher import PhraseMatcher 

phrase_matcher = PhraseMatcher(nlp.vocab)

phrases = ["swimming\nvigorously"]
patterns = [nlp(text) for text in phrases]
phrase_matcher.add("Pattern",patterns)

doc = nlp(text)
matches = phrase_matcher(doc)
matches


# In[27]:


with open("owlcreek.txt", "r") as file:
    text = file.read()

import spacy
nlp = spacy.load("en_core_web_sm")

from spacy.matcher import Matcher

matcher = Matcher(nlp.vocab)
matcher = Matcher(nlp.vocab)

pattern = [
    {'LOWER': 'swimming'}, 
    {'IS_SPACE': True, 'OP': '*'},  
    {'LOWER': 'vigorously'}
]

matcher.add("SWIMMING VIGOROUSLY", [pattern])

doc2 = nlp(text)

found_matches = matcher(doc2)
found_matches


# # Question 7

# In[28]:


#Print the text surrounding each found match.
for match_id, start, end in found_matches:
    print(f"Match: {doc2[start:end].text}")
    print(f"Surrounding text: {doc2[max(0, start-5):min(len(doc2), end+5)].text}")
    print("-" * 40)


# In[ ]:




