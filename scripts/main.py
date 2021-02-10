import requests
from bs4 import BeautifulSoup

def desplayCurrency(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    ratelist = soup.findAll("table", {"class": "ratesTable"})[0].findAll("tbody")
    for tableVal in ratelist:
        trList = tableVal.findAll('tr')
        for trVal in trList[:6]:
            print(trVal.text)


if __name__ == "__main__":
    URL = "https://www.x-rates.com/table/?from=USD&amount=1"
    desplayCurrency(URL)
