""" LEONARDO MATTHEW KNIGHT
Sua tarefa será  gerar a matriz termo documento, dos documentos recuperados da internet e
imprimir esta matriz na tela. Para tanto:
a) Considere que todas as listas de sentenças devem ser transformadas em listas de vetores,
onde cada item será uma das palavras da sentença.
b) Todos  os  vetores  devem  ser  unidos  em  um  corpus  único  formando  uma  lista  de  vetores,
onde cada item será um lexema.
c) Este único corpus será usado para gerar o vocabulário.
d) O  resultado  esperado  será  uma  matriz  termo  documento  criada  a  partir  da  aplicação  da
técnica bag of Words em todo o corpus.
"""

from corpus import pageSentences
import pandas as pd


def bagofwords():
    words = set()
    for array in pageSentences:
        for sentence in array:
            for word in sentence.split(" "):
                words.add(word)
    words = list(words)
    print("Total words: ", len(words))
    vector = []
    for array in pageSentences:
        counts = [0] * len(words)
        for sentence in array:
            for word in sentence.split(" "):
                counts[words.index(word)] += 1
        vector.append(counts)

    df = pd.DataFrame(vector, columns=words)
    print(df.head())
