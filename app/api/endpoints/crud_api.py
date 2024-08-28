from typing import Optional
from fastapi import APIRouter,Form, File, UploadFile,HTTPException
from app.crud import crud_user_data
from utils.dbconnection import collection_name
from utils.response import response
import os
from bson.objectid import ObjectId
from fastapi_pagination import Page, paginate
from fastapi_pagination.utils import disable_installed_extensions_check

disable_installed_extensions_check()

# Define the directory to save uploaded files
UPLOAD_DIRECTORY = "uploaded_files"

router = APIRouter()

accepted_file_type = ["image/png","image/jpeg","image/jpg"]

@router.post("/create_api")
async def create_api(
    name : str = Form(...),
    summery: str = Form(...),
    image: UploadFile = File(...),
):
    try:
        if image.content_type not in accepted_file_type:
            return response(1003)
        
        if os.path.exists(f"{UPLOAD_DIRECTORY}/{image.filename}"):
            return response(1009)

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
            return response(1000,user)
        
    except Exception:
        raise response(1005)

@router.get("/read_api")
def read_api() -> Page:
    try:
        users_data = crud_user_data.read(collection_name)

        return response(1004,paginate(users_data).items)

    except Exception:
        return response(1005)

@router.post("/update_api")
async def update_api(
    id:str = Form(),
    name : Optional[str] = Form(None),
    summery: Optional[str] = Form(None),
    image: Optional[UploadFile] = File(None)
):
    try:
        if image:
            if image.content_type not in accepted_file_type:
                return response(1003)

            if os.path.exists(f"{UPLOAD_DIRECTORY}/{image.filename}"):
                return response(1009)

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
            return response(1006)

    except Exception:
        return response(1005)

@router.post("/delete_api")
def delete_api(
    id:str = Form()
):
    try:
        users_data = crud_user_data.delete(collection_name,id)
        if not users_data:
            return response(1008)
        
        return response(1007)
    
    except Exception:
        return response(1005)