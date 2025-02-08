import os
from fastapi import FastAPI
<<<<<<< Updated upstream
from routes import base
=======
from dotenv import load_dotenv
load_dotenv(".env")

from routes import base

>>>>>>> Stashed changes

app = FastAPI()

app.include_router(base.base_router)
