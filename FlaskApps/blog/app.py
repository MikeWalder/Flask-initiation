from flask import Flask, render_template

from datas import Post

app = Flask(__name__)

ressources = [
    {'id':1, 'title':'Legrand', 'content':'Un des leaders mondiaux des produits et systèmes pour installations électriques et réseaux' },
    {'id':2, 'title':'Hager', 'content':'Entreprise familiale spécialisée dans les installations électriques'},
    {'id':3, 'title':'Schneider Electric', 'content':'Spécialiste et leader mondial des solutions numériques d\'énergie et des automatisations pour l\'efficacité énergétique'},
]

@app.route('/')
def home():
    return render_template('pages/index.html')

@app.route('/about')
def about():
    return render_template('pages/about.html', links=ressources)

@app.route('/pages/posts/<int:id>')
def descr_about(id):
    post = Post.find(id)
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
    app.run(debug=True, port=3000)
