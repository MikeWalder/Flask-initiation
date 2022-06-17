from flask import Flask, render_template, url_for, request

app = Flask(__name__)

# Config options - Make sure you created a 'config.py' file.
app.config.from_object('config')

from .utils import find_content

# Gestion routes
@app.route('/')
def index():
    description = "Voici une petite description"
    page_title = "Le test ultime"
    if 'img' in request.args:
        img = request.args['img']
        og_url = url_for('index', img=img, _external=True)
        og_image = url_for('static', filename=img, _external=True)
    else:
        og_url = url_for('index', _external=True)
        og_image = url_for('static', filename='tmp/sample.jpg', _external=True)
    og_description = "Découvre qui tu es en réalisant ce test !"
    return render_template('index.html',
                        user_name='Mike',
                        user_image=url_for('static', filename='img/profile.png'),
                        description=description,
                        blur=True,
                        page_title=page_title,
                        og_url=og_url,
                        og_image=og_image,
                        og_description=og_description)

@app.route('/result/')
def result():
    description = "une simple description"
    gender = request.args.get('gender')
    user_name = request.args.get('first_name')
    uid = request.args.get('id')
    profile_pic = 'http://graph.facebook.com/' + str(uid) + '/picture?type=large'
    img = 'tmp/sample.jpg'
    #og_url = url_for('index', img=img, _external=True)
    return render_template('result.html',
                        user_name=user_name,
                        user_image=profile_pic,
                        description=description)
                        #og_url=og_url)

""" @app.route('contents/<int:content_id>/')
def content(content_id):
    return content_id """
