from db import database
from fastapi import FastAPI

app = FastAPI(title="SpartanFastAPI")

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
