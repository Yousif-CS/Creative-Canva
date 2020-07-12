
from application.models import User
from application import db
import jwt

def register(email, password, first_name, last_name, birthday, gender, address, suburb, postcode):

    if db.users.find({email: email}):
        return {'status': "Email is already in use."}

    user_id = User.objects.count()
    user_id += 1
    user = User(
        user_id = user_id, 
        email = email, 
        first_name = first_name, 
        last_name = last_name,
        birthday = birthday,
        gender = gender,
        address = address,
        suburb = suburb,
        postcode = postcode,
        available = True,
        confirmed = False
    )
    user.set_password(password)

    confirm_email(email)

    id = db.Users.insertOne(user).get("insertedId")
    token = user.assign_token(id)
    return {'status': "success", 'token': token, "id": id}

# validate email
def confirm_email(email):
    return



