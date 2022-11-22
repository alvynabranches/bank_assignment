from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel

class Data(BaseModel):
    ...

app = FastAPI()

@app.get("/")
def index():
    return JSONResponse({"status": "success"}, 200)

@app.post("/")
def transaction(body: Data):
    return JSONResponse({}, 201)

@app.get("/")
def transaction(body: Data):
    return JSONResponse({}, 200)