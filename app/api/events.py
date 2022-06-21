from .core import App
from .. db.mongo import Mongo
from .. models.api import Event, Response

from pymongo.errors import PyMongoError
from fastapi import status, Response as Status

app = App()


@app.server.get("/")
async def get_events():
    """Endpoint function for getting info for index page."""
    mongo_client = Mongo("test", "events")
    objects = mongo_client.batch_get_records({})
    for o in objects:
        o.pop('_id')
    return objects


@app.server.get("/")
async def get_event():
    """Endpoint function for getting info for index page."""
    mongo_client = Mongo("test", "events")
    return mongo_client.batch_get_records({})


@app.server.post("/", response_model=Response)
async def create_event(event: Event, api_status: Status):
    """Endpoint function for getting info for index page."""
    mongo_client = Mongo("test", "events")

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
