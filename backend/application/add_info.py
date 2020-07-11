
from application.models import User
from application import db, grid_fs
import base64 

def add_info (description, encoded_url, id):
    user = db.Users.find({"_id": id})
    filename = id + "_profile_pic"
    image = base64.decodestring(encoded_url)
    db.grid_fs.put(image, filename = filename)
    db.Photos.insert({
        "_id": id,
        "photo": image
    })

    db.Users.update(
            {"_id": id}, 
            {
                "$set": {
                    "description": description
            }
        )