from crawlerpy import Get_news
from crawlerpy.resources.resources import Resources

pprint = Resources()
news = Get_news()


links = news.get_links("https://www.tehrantimes.com/page/archive.xhtml?wide=0&ms=0&pi=2&tp=697")

#links = news.get_links("https://www.tehrantimes.com/archive?tp=697", 
#                       "https://www.tehrantimes.com/page/archive.xhtml?wide=0&ms=0&pi=2",
#                       "https://www.tehrantimes.com/page/archive.xhtml?wide=0&ms=0&pi=3&tp=696")

#print(links)
pprint.pretty(links)