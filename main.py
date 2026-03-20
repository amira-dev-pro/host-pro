from fastapi import FastAPI
from routes.users import router
from database import engine, Base

app = FastAPI()

@app.get("/")
def home():

    return {"message": "Host PRO OK 🚀"} 

app.include_router(router)

Base.metadata.create_all(bind=engine) 
