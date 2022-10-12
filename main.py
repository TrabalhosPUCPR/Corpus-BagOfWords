from bs4 import BeautifulSoup
import requests

url_livros = ["https://www.gutenberg.org/files/2701/2701-h/2701-h.htm",
              "https://www.gutenberg.org/files/2097/2097-h/2097-h.htm",
              "https://www.gutenberg.org/files/68283/68283-h/68283-h.htm",
              "https://www.gutenberg.org/files/84/84-h/84-h.htm",
              "https://www.gutenberg.org/files/345/345-h/345-h.htm"]

if __name__ == '__main__':

    sentencas = []
    for url_i in range(len(url_livros)):
        res = requests.get(url_livros[url_i])
        soup = BeautifulSoup(res.text, "html5lib")
        count = 0
        words = soup.get_text().split(" ")
        sentencas.append([])
        ok = False
        sentenca = ""
        for i in range(len(words)):
            if words[i].endswith("."):
                sentenca += words[i]
                sentencas[url_i].append(sentenca)
                sentenca = ""
            elif not(words == " "):
                sentenca += words[i].replace("\n", "") + " "
    print("fim")
    print("sentencas criadas: ", end="")
    print(sentencas)
