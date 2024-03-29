from email import message
from flask import Flask, render_template, request, jsonify
# from datas import Post # importer les données du fichier data.py
import requests
import json

from datetime import datetime

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Connexion à la base de données via SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    content = db.Column(db.Text)

    def __repr__(self):
        return '<post "{}">'.format(self.title)


# Filtres personnalisés
@app.context_processor
def time_now():
    return dict(now = datetime.now())

@app.context_processor
def utility_processor():
    def pluralize(count, singular, plural=None):
        if not isinstance(count, int):
            raise ValueError('"{}" must be an integer'.format(count))
        if plural is None:
            return singular + 's'
        if count > 1:
            return plural
        if count == 1:
            return singular
    return dict(pluralize = pluralize)

# Routes
@app.route('/')
def home():
    return render_template('pages/index.html')

@app.route('/about')
def about():
    all = Post.query.all()
    return render_template('pages/about.html', links=all)

@app.route('/pages/posts/<int:id>')
def descr_about(id):
    post = Post.query.get(id) # appel à la méthode de classe 
    return render_template('pages/posts/show.html', post=post)

@app.route('/contact')
def contact():
    return render_template('pages/contact.html')

@app.route('/card')
def card():
    return render_template('pages/card.html')

@app.route('/card', methods=['POST'])
def cardAdd():
    response_object = {'status': 'success'}
    nomVille = request.form['cardName']
    #API_KEY = '4ff02ab0703b764e55577153c226ae8c'
    #url = requests.get('https://api.openweathermap.org/data/2.5/weather?q='+cardName+'&lang=fr&appid='+API_KEY)
    url_card = requests.get('https://geo.api.gouv.fr/communes?nom='+nomVille+'&fields=nom,code,codesPostaux,codeDepartement,codeRegion,population&format=json&geometry=centre')
    #json_url_card = url_card.json()
    #response_object['card'] = json_url_card
    #name_city = url_card['name']
    url_card_text = url_card.text
    url_card_json = json.loads(url_card_text)
    #return '<pre>'+url_card.text+'</pre>'
    return render_template('pages/card.html', data = url_card_json)

@app.route('/blog')
def blog():
    articles = ['First article', 'Second article', 'Third article']
    return render_template('pages/blog.html', posts=articles)

# Error handling 
@app.errorhandler(404)
def page_not_found(error):
    return render_template('errors/404.html'), 404

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, port=3000)
