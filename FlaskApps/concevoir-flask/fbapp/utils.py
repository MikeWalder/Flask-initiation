import random

from fbapp.models import Gender, Content

def find_content(gender):
    contents = Content.query.filter(Content.gender == Gender[gender]).all()
    return random.choice(contents)