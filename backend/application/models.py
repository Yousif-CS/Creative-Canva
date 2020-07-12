import flask
from application import db
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
class User(db.Document):
    user_id     =   db.IntField(unique=True)
    first_name  =   db.StringField(max_length=20)
    last_name   =   db.StringField(max_length=20)
    email       =   db.EmailField(max_length=30, unique=True)
    birthday    =   db.DateField()
    gender      =   db.StringField()
    address     =   db.StringField()
    suburb      =   db.StringField()
    postcode    =   db.IntField(length=4)
    description =   db.StringField(max_length = 200)
    password    =   db.StringField(max_length=20)
    available   =   db.BooleanField(default=True)
    token       =   db.StringField()
    contacts    =   db.ListField(Contact)
    # profile_pic =   
    
    def set_password(self, password):
        self.password = generate_password_hash(password)

    def get_password(self, password):
        return check_password_hash(self.password, password)   

    def assign_token(self, id):
        secret = 'YUWA'
        token = str(jwt.encode({'id': id}, secret, algorithm='HS256'))
        self.token = token
        db.Users.update(
            {"_id": id}, 
            {$set: {"token": token}}
        )
        return token

    def invalidate_token(self, token):
        self.token = ""

# class Photo(db.Document):
#     photo = FileField()
#     id = ObjectId()

# class Course(db.Document):
#     courseID   =   db.StringField( max_length=10, unique=True )
#     title       =   db.StringField( max_length=100 )
#     description =   db.StringField( max_length=255 )
#     credits     =   db.IntField()
#     term        =   db.StringField( max_length=25 )

# class Enrollment(db.Document):
#     user_id     =   db.IntField()
#     courseID    =   db.StringField( max_length=10 )
