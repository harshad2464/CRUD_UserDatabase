from pathlib import Path
from fastapi import FastAPI, APIRouter
from app.api.api import api_router
from fastapi.staticfiles import StaticFiles

BASE_PATH = Path(__file__).resolve().parent
root_router = APIRouter()
app = FastAPI(title="Test REST API. V1")

UPLOAD_DIRECTORY = "uploaded_files"
Path(UPLOAD_DIRECTORY).mkdir(parents=True, exist_ok=True)

app.mount("/files", StaticFiles(directory=UPLOAD_DIRECTORY), name="files")

app.include_router(api_router)


if __name__ == "__main__":
    import uvicorn
    # Use this for debugging purposes only       
    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")
    # uvicorn.main()