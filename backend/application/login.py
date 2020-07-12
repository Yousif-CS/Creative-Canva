
from application.models import User
from application import db

def login(email, password):
    user_exists = db.users.find({email: email}, password)
    if not user_exists:
        return {'status': "Email does not exist"}
    
    unhashed_pw = user_exists.get_password(password)
    if unhashed_pw != password:
        return "Invalid password"

    # need to make new token
    token = user_exists.get(token)
    id = user_exists.get(_id)
  
    return {'status': "success", 'token': token, "id": id}
