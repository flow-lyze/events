import json
import bson
import logging

from models.api import Event, Response
from utils.api import edit_event_object
from utils.exceptions import MongoNotFoundError, MongoOperationWithoutAffectError
from utils.log import LogConfig

from logging.config import dictConfig
from db.mongo import Mongo
from pymongo.errors import PyMongoError
from fastapi import Request, status, Response as Status, FastAPI, APIRouter


dictConfig(LogConfig)
logger = logging.getLogger("")
app = FastAPI(debug=True)

router = APIRouter()


@router.get("/")
async def get_events(request: Request):
    """Endpoint function for getting info for index page."""
    mongo_client = Mongo()
    objects = mongo_client.batch_get_records({})
    for o in objects:
        o["_id"] = str(o["_id"])
    return objects


@router.post("/", response_model=Response)
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


@router.put("/")
async def edit_event(request: Request, api_status: Status):
    """Endpoint function for editing event information."""
    # request body is a coroutine, so we have to await this
    body = await request.body()
    body = json.loads(body.decode("utf-8").replace("'", '"'))

    try:
        await edit_event_object(body)
        response = Response(status_code=status.HTTP_200_OK, message="Object was successfully edited.")
        api_status.status_code = status.HTTP_200_OK
    except bson.errors.InvalidId as err:
        err_msg = f"Got error, while editing record, should be a valid `ObjectID` string: {err}"
        logger.error(err_msg)
        response = Response(
            status_code=status.HTTP_400_BAD_REQUEST, message=err_msg
        )
        api_status.status_code = status.HTTP_400_BAD_REQUEST
    except MongoNotFoundError as err:
        response = Response(status_code=status.HTTP_404_NOT_FOUND, message=str(err))
        api_status.status_code = status.HTTP_404_NOT_FOUND
    except MongoOperationWithoutAffectError as err:
        response = Response(status_code=status.HTTP_202_ACCEPTED, message=str(err))
        api_status.status_code = status.HTTP_202_ACCEPTED

    return response


app.include_router(router)