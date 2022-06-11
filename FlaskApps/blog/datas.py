from flask import abort

class Post():
    RESSOURCES = [
        {'id':1, 'title':'Legrand', 'content':'Un des leaders mondiaux des produits et systèmes pour installations électriques et réseaux' },
        {'id':2, 'title':'Hager', 'content':'Entreprise familiale spécialisée dans les installations électriques'},
        {'id':3, 'title':'Schneider Electric', 'content':'Spécialiste et leader mondial des solutions numériques d\'énergie et des automatisations pour l\'efficacité énergétique'},
        {'id':4, 'title':'CGED', 'content':'Matériel électrique pour professionnels'},
    ]

    @classmethod # pour appeler la méthode sans pour autant créer une instance de classe 
    def all(cls):
        # Fetch all ressources 
        return cls.RESSOURCES

    @classmethod
    def find(cls, id):
        # Fetch Ressource by id
        try:
            return cls.RESSOURCES[int(id) - 1]
        except IndexError: # cas où le paramètre d'entrée est autre que int
            abort(404)

