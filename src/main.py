
from typing import Union

from fastapi import FastAPI
import redis

app = FastAPI()

r = redis.Redis(host="redis",port=6379)

@app.get("/")
def read_root():
    return {"Hello": "Hello "}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/hits")
def read_root():
    r.inc("hits")
    return {"number of hits": r.get("hits")}