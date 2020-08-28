from crawlerpy.crawlerpy import Get_news
from crawlerpy.resources.resources import Resources

pprint = Resources()
news = Get_news()

keyword_list = ['Development','Plan','Persian','Zataria'] # If it prints an empty list maybe is because the news that contains these words are in another page
news_to_find = news.find(keyword_list, pi=2, tp='Society')

#pprint.pretty(previews)
print(news_to_find)