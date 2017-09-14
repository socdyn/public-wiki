#Tom Davidson 21/11/2016
import pandas as pd
from corenlp_pywrap import pywrap

if __name__ == '__main__':
    cn = pywrap.CoreNLP(url='http://localhost:9000', annotator_list=['ner'])
    data = input("Please enter a sentence for classification: ")
    D = cn.arrange(data)
    #We can loop through the values to see the words and the corresponding entities.
    words = D['word']
    entities = D['ner']
    for i in range(0, len(D['word'])):
        print(words[i], entities[i])
