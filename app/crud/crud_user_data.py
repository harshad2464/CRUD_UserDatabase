from bson.objectid import ObjectId

def create(collection_name,user_data):
    item = collection_name.insert_one(user_data)
    new_item = collection_name.find_one({"_id": item.inserted_id})
    new_item ={
        "id":str(new_item['_id']),
        "Name":new_item['name'],
        "image_file":new_item['image'],
        "summery":new_item['summery'],
    }
    return new_item
    
def read(collection_name):
    all_data = []
    items = collection_name.find()
    for item in items:
        all_data.append(
            {
                "id":str(item['_id']),
                "Name":item['name'],
                "image_file":item['image'],
                "summery":item['summery'],
            }
        )
    return all_data

def update(collection_name,id,user_data):
    data = collection_name.find({"_id":ObjectId(id)})
    if data:
        updated_item = collection_name.update_one(
            {"_id": ObjectId(id)}, {"$set": user_data}
        )
        if updated_item:
            return True
        return False 

def delete(collection_name,id):
    user_data = collection_name.find({"_id":ObjectId(id)})
    if user_data:
        collection_name.delete_one({"_id": ObjectId(id)})
        return True
    else:
        return False 