from .core import App
from .. db.mongo import Mongo
from .. models.api import Event, Response

from pymongo.errors import PyMongoError
from fastapi import Request, status, Response as Status

app = App()


@app.server.get("/")
async def get_events(request: Request):
    """Endpoint function for getting info for index page."""
    mongo_client = Mongo()
    objects = mongo_client.batch_get_records({})
    for o in objects:
        o["_id"] = str(o["_id"])
    return objects


@app.server.get("/")
async def get_event(request: Request):
    """Endpoint function for getting info for index page."""
    mongo_client = Mongo()
    return mongo_client.batch_get_records({})


@app.server.post("/", response_model=Response)
async def create_event(event: Event, api_status: Status):
    """Endpoint function for getting info for index page."""
    mongo_client = Mongo()

    try:
        mongo_client.create_new_record(dict(event))
        response = Response(
            status_code=status.HTTP_201_CREATED, message=f"Event: {event.name} successfully created."
        )
        api_status.status_code = status.HTTP_201_CREATED
    except PyMongoError as e:
        print(f"Got error: {e}")
        response = Response(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, error="Database Issue, cannot create new event."
        )
        api_status.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    return response
