from application.models import User
from application import db, grid_fs
import base64 

def add_contact (friend_id):
    user = db.Users.find({"_id": id})
    filename = id + "_profile_pic"
    image = base64.decodestring(encoded_url)
    db.grid_fs.put(image, filename = filename)
    db.Photos.insert({
        "_id": id,
        "photo": image
    })

    User (
        Contacts: [
            {
                "_id": friend_id,
                "confirmed"
            }
        ]
    )