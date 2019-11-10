#https://automatetheboringstuff.com/chapter11/
import requests
import bs4


def Scraper(question):
    question = question.lower()
    question = question.replace(" ","+")
    linkList = []
    res = requests.get('https://google.com/search?q='+question+'+site%3Astackoverflow.com')
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    for link in soup.find_all('a' , href = True):
        if link['href'] != "#":
            if "https://stackoverflow.com" in link["href"]:
                linkList.append(link["href"])
       
    return linkList