from typing import Optional
from fastapi import APIRouter,Form, File, UploadFile
from app.crud import crud_user_data
from utils.dbconnection import collection_name
import os
from bson.objectid import ObjectId

# Define the directory to save uploaded files
UPLOAD_DIRECTORY = "uploaded_files"

router = APIRouter()

@router.post("/create_api")
async def create_api(
    name : str = Form(...),
    summery: str = Form(...),
    image: UploadFile = File(...),
):
    try:
        file_location = os.path.join(UPLOAD_DIRECTORY, image.filename)
        with open(file_location, "wb") as file_object:
            file_object.write(await image.read())
        
        user_data={
            "name":name,
            "image":f"files/{image.filename}",
            "summery":summery
        }
        user = crud_user_data.create(collection_name,user_data)
        if user:
            return {
                "Message":"User Created Successfully",
                "Data":user
            }
        
    except Exception as e:
        raise e

@router.post("/read_api")
def read_api():
    users_data = crud_user_data.read(collection_name)
    return users_data

@router.post("/update_api")
async def update_api(
    id:str = Form(),
    name : Optional[str] = Form(None),
    summery: Optional[str] = Form(None),
    image: Optional[UploadFile] = File(None)
):
    if image:
        file_location = os.path.join(UPLOAD_DIRECTORY, image.filename)
        with open(file_location, "wb") as file_object:
            file_object.write(await image.read())
    if id:
        data = collection_name.find_one({"_id":ObjectId(id)})

    user_data={
        "name":name if name else data['name'],
        "image":f"files/{image.filename}" if image else data['image'],
        "summery":summery if summery else data['summery']
    }
    update_data = crud_user_data.update(collection_name,id,user_data)

    if update_data:
        return {
            "message": "Data Update Successfully"
        }

@router.post("/delete_api")
def delete_api(
    id:str = Form()
):

    users_data = crud_user_data.delete(collection_name,id)
    if users_data:
        return {"Message": "Data Deleted Successfully."}
    return users_data