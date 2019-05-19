from flask import render_template
from app import app
@app.route('/')
def index():
    """
    Function that returns the index page and its data
    """
    title ='Home-Everywhere,Everytime News Room'
    return render_template ('index.html',title = title)
@app.route('/newssites/<news_id>')
def newssites(news_id):
    """
    Function that returns a news site and its details
    """
    return render_template ('newssite.html',id = news_id)