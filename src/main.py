from fastapi import FastAPI

import redis

red = redis.Redis(host="localhost", port=6379)
app = FastAPI()

# import debugpy

# debugpy.listen(("0.0.0.0", 5678))
# print("Waiting for client to attach...")
# debugpy.wait_for_client()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/hits")
def read_root():
    red.set("foo", "bar")
    red.incr("hits")
    return {"Number of hits:": red.get("hits"), "foo": red.get("foo")}



