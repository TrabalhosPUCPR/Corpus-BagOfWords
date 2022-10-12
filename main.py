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
