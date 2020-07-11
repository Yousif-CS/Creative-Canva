from application import db


# search only in subrub
# get token
def search (first_name, last_name, id):
    suburb = db.Users.find({"_id": id}, suburb)

    community = db.Users.find({
                    # first_name: first_name, 
                    # last_name: last_name, 
                    suburb: suburb,
                    available: {$exists: True}
                })
    collection = community.sort({first_name: first_name, last_name: last_name}).pretty()
    return {"users": collection}
