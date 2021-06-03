import os

from cryptography.fernet import Fernet
from dotenv import load_dotenv
from fastapi import FastAPI
from mongoengine import connect
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()

connect(host="mongodb://{}:{}@{}:{}/{}".format(
    os.getenv('MONGO_INITDB_ROOT_USERNAME'),
    os.getenv('MONGO_INITDB_ROOT_PASSWORD'),
    os.getenv('MONGO_HOST'),
    '27017',
    os.getenv('MONGO_INITDB_DATABASE')
))

SECRET_KEY = os.getenv('SECRET_KEY')

fernet = Fernet(SECRET_KEY)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
