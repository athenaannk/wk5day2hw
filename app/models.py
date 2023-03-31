from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash

db= SQLAlchemy()


pokesquadTable = db.Table(
    'pokesquadTable',
    db.Column('name', db.String, db.ForeignKey('pokemon.name'), nullable=False),
    db.Column('id', db.Integer, db.ForeignKey('user.id'), nullable=False)
)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    wins = db.Column(db.Integer, default=0)
    losses = db.Column(db.Integer, default=0)
    ties = db.Column(db.Integer, default=0)
    squad = db.relationship('Pokemon',
        secondary = 'pokesquadTable',
        backref = 'squad',
        lazy = 'dynamic')

    def __init__(self, username, email, password, wins, losses, ties):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password) 
        self.wins = wins
        self.losses = losses
        self.ties = ties

    def saveUser(self):
        db.session.add(self)
        db.session.commit()
    
    def catchPokemon(self, pokemon):
        self.squad.append(pokemon)
        db.session.commit()
    
    def releasePokemon(self, pokemon):
        self.squad.remove(pokemon)
        db.session.commit()

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    img_url = db.Column(db.String)
    body = db.Column(db.String)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self, title, img_url, body, user_id):
        self.title = title
        self.img_url = img_url
        self.body = body
        self.user_id = user_id

class Pokemon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    base_xp = db.Column(db.String)
    front_shiny = db.Column(db.String)
    base_atk = db.Column(db.String)
    base_hp = db.Column(db.String)
    base_def = db.Column(db.String)


    def __init__(self, name, base_xp, front_shiny, base_atk, base_hp, base_def):
        self.name = name
        self.base_xp = base_xp
        self.front_shiny = front_shiny
        self.base_atk = base_atk
        self.base_hp = base_hp
        self.base_def = base_def

    def savePokemon(self):
        db.session.add(self)
        db.session.commit()

    def catchPokemon(self, user):
        db.session.append()
        db.session.commit()
    
    def releasePokemon(self, user):
        self.liked.remove()
        db.session.commit()
