import requests
from bs4 import BeautifulSoup

adres = "http://trojmiasto.pl"

response = requests.get(adres)

print(response.status_code)

response.raise_for_status()

# print(response.text)

# trojmiasto_zupa = BeautifulSoup(response.text, "html.parser")
# print(trojmiasto_zupa.title)
# motto = trojmiasto_zupa.select(".motto-box-wrap a")
# print(motto)

# for link in linki:
    # print(link.getText())
    # # print(str(link))
    # print(link.attrs)
    #
# print(f"Motto: {motto[0].get('title')}")
    # print(link.get("href"))
    # print("------------------\n")

trójmiasto_newslist = BeautifulSoup(response.text, "html.parser")
print(trójmiasto_newslist.title)
newslist = trójmiasto_newslist.select(".news-first a")
# newslist = trójmiasto_newslist.select(".news-fist a")
print(newslist)




for news in newslist:
    print(f"News: {news.getText()}")

for news in newslist:
    print(news.attrs['href'])