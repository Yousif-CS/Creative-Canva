import flask
from application import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Document):
    user_id     =   db.IntField( unique=True )
    first_name  =   db.StringField( max_length=20 )
    last_name   =   db.StringField( max_length=20 )
    email       =   db.StringField( max_length=30, unique=True )
    password    =   db.StringField( max_length=20 )
    address     =   db.StringField( max_length=30 )
    suburb      =   db.StringField( max_length=15 )
    available   =   db.BooleanField( default=True )
    
    def set_password(self, password):
        self.password = generate_password_hash(password)

    def get_password(self, password):
        return check_password_hash(self.password, password)    
