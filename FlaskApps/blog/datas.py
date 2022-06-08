from flask import abort

class Post():
    RESSOURCES = [
        {'id':1, 'title':'Legrand', 'content':'Un des leaders mondiaux des produits et systèmes pour installations électriques et réseaux' },
        {'id':2, 'title':'Hager', 'content':'Entreprise familiale spécialisée dans les installations électriques'},
        {'id':3, 'title':'Schneider Electric', 'content':'Spécialiste et leader mondial des solutions numériques d\'énergie et des automatisations pour l\'efficacité énergétique'},
    ]

    @classmethod
    def all(cls):
        # Fetch all ressources 
        return cls.RESSOURCES

    @classmethod
    def find(cls, id):
        # Fetch Ressource by id
        try:
            return cls.RESSOURCES[int(id) - 1]
        except IndexError:
            abort(404)

