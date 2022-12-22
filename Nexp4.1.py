from nltk import *
sample_text="""Even sunshine feels bit warmer when I am around you"""
tokens = word_tokenize(sample_text)
tagged_words=pos_tag(tokens)
print(tagged_words)
chunker =(
   r'''
   NP:{<NN.?>*<VBD.?>*<JJ.?>*<CC>?}
   VB:{<VB.*>}
   ''')
chunkParser=RegexpParser(chunker)
chunked=chunkParser.parse(tagged_words)
print(chunked)
chunked.draw()
