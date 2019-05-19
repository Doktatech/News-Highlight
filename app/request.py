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
