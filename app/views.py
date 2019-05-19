from flask import render_template
from app import app
from .request import get_news
@app.route('/')
def index():
    """
    Function that returns the index page and its data
    """
    news_sources = get_news('name')
    print (news_sources)
    title ='Home-Everywhere,Everytime News Room'
    return render_template ('index.html',title = title, news_source= news_sources)
@app.route('/newssites/<news_id>')
def newssites(news_id):
    """
    Function that returns a news site and its details
    """
    return render_template ('newssite.html',id = news_id)