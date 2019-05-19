from flask import render_template
from app import app
@app.route('/')
def index():
    """
    Function that returns the index page and its data
    """
    Greetings= "Goodmorning Albazeera"
    return render_template ('index.html', Greeting=Greetings)