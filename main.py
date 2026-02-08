from fastapi import FastAPI
from database import engine
import models
from router import user, auth, post

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(user.router)

app.include_router(auth.router)

app.include_router(post.router)

@app.get("/")
def home():
    return {"message": "Blog API is running "}
