from fastapi import FastAPI

from db import database

app = FastAPI(title="SpartanFastAPI")


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
