from app import app
import urllib.request,json
from .models import news
api_key=app.config['NEWS_API_KEY']
base_url=app.config['NEWS_API_BASE_URL']
def get_news(category):
    """
    Functionfor getting the json response from our API request
    """
    get_news_url = base_url.format(category,api_key)
    with urllib.request.urlopen(get_news_url) as url:
        get_news_data =url.read()
        get_news_response =json.loads(get_news_data)

        news_results =None
        if get_news_response =get_news_response['results']
        return news_results
def process_results (news_list)
    """
    A function to process retrieved news result and display them on a list
    """
     news_results =[]
     for news_item in news_list:
        id=news_item.get('id')
        title= news_item.get('title')
        overview = news_item.get('overview')
        poster = news_item.get('poster_path')
        vote_average = news_item.get('vote_average')
        vote_count = news_item.get('vote_count')

        if poster:
            news_object = News(id,title,overview,poster,vote_average,vote_count)
            news_results.append(news_object)

    return news_results