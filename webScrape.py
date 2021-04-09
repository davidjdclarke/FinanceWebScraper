import requests
from bs4 import BeautifulSoup

def getID(url, id, headers):
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    extract = soup.find(id=id).get_text()
    value = ''
    print('Extracted Data: ' + extract)

    for x in range(len(extract)):
        # print(value[x:x+9])
        if extract[x-9:x] == 'watchlist':
            for i in range(20):
                if extract[x+i] == '-' or extract[x+i] == '+':
                    value = extract[x:x+i]
                    break

    print("Return Data: $" + value)

    value = value.replace(',', "")

    return float(value)


#temp = getID(URL, ID, Headers)


if __name__ == "__main__":

    Headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
    ID = 'quote-header-info'

    url1 = "https://finance.yahoo.com/quote/CADUSD=x"
    url2 = 'https://finance.yahoo.com/quote/AAPL?p=AAPL'
    url3 = 'https://finance.yahoo.com/quote/GOOG?p=GOOG&.tsrc=fin-srch'
    url4 = 'https://finance.yahoo.com/quote/KO?p=KO'

    temp1 = getID(url1, ID, Headers)
    temp2 = getID(url2, ID, Headers)
    temp3 = getID(url3, ID, Headers)
    temp4 = getID(url4, ID, Headers)

