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
