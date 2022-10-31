""" LEONARDO MATTHEW KNIGHT
Sua tarefa será gerar a matriz termo documento, dos documentos recuperados da internet e
imprimir esta matriz na tela. Para tanto:
a) Considere que todas as listas de sentenças devem ser transformadas em listas de vetores,
onde cada item será uma das palavras da sentença.
b) Todos os vetores devem ser unidos em um corpus único formando uma lista de vetores,
onde cada item será um lexema.
c) Este único corpus será usado para gerar o vocabulário.
d) O resultado esperado será uma matriz termo documento criada a partir da aplicação da
técnica bag of Words em todo o corpus.
"""

from bs4 import BeautifulSoup
import requests
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

urls = ["https://www.sas.com/en_us/insights/analytics/what-is-natural-language-processing-nlp.html",
        "https://hbr.org/2022/04/the-power-of-natural-language-processing",
        "https://monkeylearn.com/natural-language-processing/",
        "https://www.tableau.com/learn/articles/natural-language-processing-examples",
        "https://towardsdatascience.com/your-guide-to-natural-language-processing-nlp-48ea2511f6e1"]
vec = CountVectorizer()

if __name__ == '__main__':
    sentencas = []
    for j in range(len(urls)):
        res = requests.get(urls[j])
        soup = BeautifulSoup(res.text, "html5lib")
        words = soup.get_text().split(" ")
        sentencas.append([])
        sentenca = ""
        for i in range(len(words)):
            words[i] = words[i].replace("\n", "")
            if not (words[i].isalpha()) and not (words[i].isdigit()):
                if not (sentenca == ""):
                    sentencas[j].append(sentenca)
                    sentenca = ""
            elif not (words[i].isspace()):
                sentenca += words[i] + " "
        X = vec.fit_transform(sentencas[len(sentencas) - 1])
        df = pd.DataFrame(X.toarray(), columns=vec.get_feature_names_out())
        df.head()
        print(df)
