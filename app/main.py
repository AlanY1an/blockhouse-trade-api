from fastapi import FastAPI
from .database import engine, Base
from .routes import router

app = FastAPI()

# create database tables
Base.metadata.create_all(bind=engine)

# register routes
app.include_router(router)
