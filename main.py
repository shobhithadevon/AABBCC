
from fastapi import FastAPI 
import models as models
from configparser import engine
import router

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
async def Home():
    return "welcome Home"

app.include_router(router.router,pefix="/school",tags=["school"])