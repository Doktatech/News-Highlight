from flask import render_template, request, redirect, url_for
from . import main
from ..request import get_sources, get_articles


@main.route('/')
def index():
    """View root page function that returns index page """
    title = 'Everywhere,Everytime News'
    # Getting the news sources
    news_sources = get_sources('sources')
    return render_template('index.html', title=title, news_sources=news_sources)


@main.route('/articles/<source_id>')
def source(source_id):
    """
    View for top story articles on from request
    """
    # articles = get_articles('articles')
    source_and_articles = get_articles(source_id)
    return render_template('articles.html', source_and_articles=source_and_articles)
