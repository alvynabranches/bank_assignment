import sys
import router
from db import engine
from models import Base
from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.responses import JSONResponse

if sys.version_info.major == 3 and sys.version_info.minor >= 10:
    import collections
    setattr(collections, "MutableMapping", collections.abc.MutableMapping)

app = FastAPI()
Base.metadata.create_all(bind=engine)

@app.get("/")
async def index(request: Request):
    return JSONResponse({"status": "Working"})

app.include_router(router.route)