from crawlerpy.crawlerpy import Get_news
from resources.resources import Resources

pprint = Resources()
news = Get_news()

previews = news.get_previews("https://www.tehrantimes.com/page/archive.xhtml?wide=0&ms=0&pi=2",
                             "https://www.tehrantimes.com/archive?tp=697")

#previews = news.get_previews(pi=1,tp='Politics',ms=0,dy=10,mn=2,yr=2019)
#previews = news.get_previews(pi=4,tp='sports',mn=5,yr=2020)

#print(previews)
pprint.pretty(previews)