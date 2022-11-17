""" LEONARDO MATTHEW KNIGHT
Sua tarefa será gerar a matriz termo-documento usando TF-IDF por meio da aplicação das 
fórmulas  TF-IDF  na  matriz  termo-documento  criada  com  a  utilização  do  algoritmo  Bag of 
Words. Sobre o Corpus que recuperamos anteriormente. O entregável desta tarefa é uma 
matriz termo-documento onde a primeira linha são os termos e as linhas subsequentes são 
os vetores calculados com o TF-IDF. 
2. Sua tarefa será gerar uma matriz de distância, computando o cosseno do ângulo entre todos 
os vetores que encontramos usando o tf-idf. Para isso use a seguinte fórmula para o cálculo 
do  cosseno  use  a  fórmula  apresentada  em  Word2Vector  (frankalcantara.com) 
(https://frankalcantara.com/Aulas/Nlp/out/Aula4.html#/0/4/2)  e  apresentada  na  figura  a 
seguir:  

O resultado deste trabalho será uma matriz que relaciona cada um dos vetores já calculados 
com todos os outros vetores disponíveis na matriz termo-documento mostrando a distância 
entre cada um destes vetores. 
"""

import sklearn.feature_extraction.text as sk
from bagofwords import countVector
from corpus import pageSentences
import pandas as pd
import numpy as np


def calc_tf_idf():
    sentences = []
    for array in pageSentences:
        pageallsentences = ""
        for s in array:
            pageallsentences += s + " "
        sentences.append(pageallsentences)
    print("Calculando tf_idf")
    vectorizer = sk.TfidfVectorizer()
    vectors = vectorizer.fit_transform(sentences)
    denselist = vectors.todense().tolist()
    df = pd.DataFrame(denselist, columns=vectorizer.get_feature_names_out())
    print("tfIdf: ")
    print(df)

    for vetor in range(len(countVector)):
        for vetor2 in range(vetor+1, len(countVector)):
            cos_sim = np.dot(countVector[vetor], countVector[vetor2]) / (np.linalg.norm(countVector[vetor]) * np.linalg.norm(countVector[vetor2]))
            print(f"Cosseno do vetor {vetor} com o vetor {vetor2}: {cos_sim}")
