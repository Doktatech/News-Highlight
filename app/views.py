from flask import render_template
from app import app
@app.route('/')
def index():
    """
    Function that returns the index page and its data
    """
    Greetings= "Goodmorning Albazeera"
    return render_template ('index.html', Greeting=Greetings)
@app.route('/newssites/<news_id>')
def newssites(news_id):
    """
    Function that returns a news site and its details
    """
    return render_template ('newssite.html',id = news_id)