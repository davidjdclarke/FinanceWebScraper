import webScrape as webs
import toExcel as xl
from openpyxl import load_workbook
import requests
from bs4 import BeautifulSoup
import datetime


def main():

    headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'}
    filename = "C:\\Users\\david\\Documents\\Investments\\Personal\\Personal Finances.xlsx"

    xl.toXl(filename, 'A1', str(datetime.datetime.now().date()))

    stock = {"APPL":     ["https://finance.yahoo.com/quote/AAPL?p=AAPL", 'quote-header-info', 0, "F17"],
             "GOOG":     ["https://finance.yahoo.com/quote/GOOG?p=GOOG&.tsrc=fin-srch", 'quote-header-info', 0, "F19"],
             "FB":       ["https://finance.yahoo.com/quote/FB?p=FB&.tsrc=fin-srch", 'quote-header-info', 0, "F18"],
             "KO":       ["https://finance.yahoo.com/quote/KO?p=KO", 'quote-header-info', 0, "F20"],
             "cad/usd":  ["https://finance.yahoo.com/quote/CADUSD=x", 'quote-header-info', 0, "H4"]}

    new_stocks = updateValues(stock, headers)
    updateSheet(new_stocks, filename)
    print(new_stocks)


def updateValues(dict, user_agent):
    for x in dict:
        dict[x][2] = webs.getID(dict[x][0], dict[x][1], user_agent)
    return dict


def updateSheet(new_stocks, filename):
    for x in new_stocks:
        xl.toXl(filename, new_stocks[x][3], new_stocks[x][2])


if __name__ == "__main__":
    main()
