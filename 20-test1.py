import urllib.request
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self,site):
        self.site = site

    def scrape(self):
        r = urllib.request.urlopen(self.site)
        html = r.read()
        parser = "html.parser"
        sp = BeautifulSoup(html,parser)
        with open("output.txt", "w") as f:
            for tag in sp.find_all("a"):
                url = tag.get("href")
                if url is None:
                    continue
                if "articles" in url:
                    print("\n" +  "https://news.google.com/" + url.replace("./",""))
                    f.write("https://news.google.com/" + url.replace("./","") + "\n")

news = "https://news.google.com/topstories?hl=ja&gl=JP&ceid=JP:ja"
Scraper(news).scrape()


