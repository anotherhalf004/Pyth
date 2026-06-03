import requests
import json
from newsapi import NewsApiClient

newsapi = NewsApiClient(api_key='your_api_key')

def get_news():

    all_articles = newsapi.get_everything(
                                        q = 'nvidia',
                                        from_param='2026-05-23',
                                        to='2026-06-03',
                                        language='en',
                                        sort_by='popularity'
                                        )
    if len(all_articles.get('totalResults'))!=0:
        print(json.dumps(all_articles,indent=4))
    else:
        print("Not found")


# print(all_articles)
sources = newsapi.get_sources()
# print(json.dumps(top_headlines,indent=4)) # prettty json hehe



def get_top_headlines():
    query = str(input("Enter keyword for which top headline to read : "))

    top_headlines = newsapi.get_top_headlines(
                                            q = query,
                                            language= 'en',
                                            country= 'us',
                                            category='technology',
                                        )
    articles = top_headlines.get('articles',[])
    if not articles:
        print(f"No articles found for {query}")

    for i,article in enumerate(articles):
        content = article.get('content','No content')
        print(f'Content for article {i+1} : {content}\n')



l = int(input("Enter : 1 - For top headlines\n\t2 - For normal news\n"))
#
if l == 1 :
    get_top_headlines()
else:
    get_news()
    

