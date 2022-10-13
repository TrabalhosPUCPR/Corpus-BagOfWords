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

url_livros = ["https://www.sas.com/en_us/insights/analytics/what-is-natural-language-processing-nlp.html",
              "https://hbr.org/2022/04/the-power-of-natural-language-processing",
              "https://monkeylearn.com/natural-language-processing/",
              "https://www.tableau.com/learn/articles/natural-language-processing-examples",
              "https://towardsdatascience.com/your-guide-to-natural-language-processing-nlp-48ea2511f6e1"]

if __name__ == '__main__':
    sentencas = []
    for j in range(len(url_livros)):
        res = requests.get(url_livros[j])
        soup = BeautifulSoup(res.text, "html5lib")
        words = soup.get_text().split(" ")
        sentencas.append([])
        sentenca = ""
        for i in range(len(words)):
            if words[i].endswith("."):
                sentenca += words[j]
                sentencas[j].append(sentenca)
                sentenca = ""
            elif not(words[i].isspace()):
                sentenca += words[i].replace("\n", "") + " "
