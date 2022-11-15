""" LEONARDO MATTHEW KNIGHT
Sua  tarefa  será  transformar  um  conjunto  de  5  sites,  sobre  o  tema  de  processamento  de
linguagem natural em um conjunto de cinco listas distintas de sentenças. Ou seja, você fará uma função
que, usando a biblioteca Beautifull Soap, faça a requisição de uma url, e extrai todas as sentenças desta
url. Duas condições são importantes:
a) A página web (url) deve apontar para uma página web em inglês contendo, não menos que
1000 palavras.
b) O texto desta página deverá ser transformado em um array de senteças.

Para separar as sentenças você pode usar os sinais de pontuação ou as funções da biblibioteca
Spacy.
"""

from bs4 import BeautifulSoup
import requests
import re

urls = ["https://www.sas.com/en_us/insights/analytics/what-is-natural-language-processing-nlp.html",
        "https://hbr.org/2022/04/the-power-of-natural-language-processing",
        "https://monkeylearn.com/natural-language-processing/",
        "https://www.tableau.com/learn/articles/natural-language-processing-examples",
        "https://towardsdatascience.com/your-guide-to-natural-language-processing-nlp-48ea2511f6e1"]
pageSentences = []


def separatetext(t):
    t = re.sub(r"[\n\t]", "", t)
    # https://stackoverflow.com/a/25736082 peguei esse regex pra separar em sentenca daqui
    s = re.split("(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s", t)
    s = [sent.strip(" ") for sent in s]
    return s


def corpus():
    n = 0
    for url in urls:
        html = requests.get(url)
        bs = BeautifulSoup(html.text, "html.parser")
        text = bs.find_all("p")
        pageSentences.append([])
        for te in text:
            for result in separatetext(te.get_text()):
                if result != '':
                    pageSentences[n].append(result)
        n += 1
