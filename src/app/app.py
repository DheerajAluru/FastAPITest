from fastapi import FastAPI, status, HTTPException, Depends, UploadFile,File, Request, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder
from src.routes.eda import Eda
from src.routes.items import router

app = FastAPI(title="EDA REST API",
              debug=True)


# origins = [
#     'http://localhost:3000'
# ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    router,
    tags=["API Call Router"]
)


 




    





