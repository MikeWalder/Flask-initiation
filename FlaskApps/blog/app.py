from flask import Flask, render_template

# from datas import Post # importer les données du fichier data.py

from datetime import datetime

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    content = db.Column(db.Text)

ressources = [
    {'id':1, 'title':'Legrand', 'content':'Un des leaders mondiaux des produits et systèmes pour installations électriques et réseaux' },
    {'id':2, 'title':'Hager', 'content':'Entreprise familiale spécialisée dans les installations électriques'},
    {'id':3, 'title':'Schneider Electric', 'content':'Spécialiste et leader mondial des solutions numériques d\'énergie et des automatisations pour l\'efficacité énergétique'},
]

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
        return 's'
    return dict(pluralize = pluralize)

@app.route('/')
def home():
    return render_template('pages/index.html')

@app.route('/about')
def about():
    return render_template('pages/about.html', links=ressources)

@app.route('/pages/posts/<int:id>')
def descr_about(id):
    post = Post.query.get(id) # appel à la méthode de classe 
    return render_template('pages/posts/show.html', post=post)

@app.route('/contact')
def contact():
    return render_template('pages/contact.html')

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
