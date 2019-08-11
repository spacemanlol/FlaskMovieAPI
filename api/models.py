from . import db

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    rating = db.Column(db.Integer)

# from api.models import Movie
# from api import db, create_app
# db.create_all(app=create_app())