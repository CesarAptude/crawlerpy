from crawlerpy.crawlerpy import Get_news
from crawlerpy.resources.resources import Resources

pprint = Resources()
news = Get_news()


elements = news.get_elements("https://www.tehrantimes.com/news/451619/Medicinal-plants-hold-potential-for-realizing-surge-in-production")

#elements = news.get_elements("https://www.tehrantimes.com/news/451525/A-glimpse-of-Muharram-mourning-rituals-across-Iran-Bil-Zani",
#                             "https://www.tehrantimes.com/news/451659/Energy-efficient-households-to-get-100-discount-on-electricity",
#                             "https://www.tehrantimes.com/news/451604/Incentive-packages-help-energy-ministry-pass-summer-without-blackouts")

#print(elements)
pprint.pretty(elements)