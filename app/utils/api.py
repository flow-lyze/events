import logging

from db.mongo import Mongo
from models.api import Event
from utils.exceptions import MongoNotFoundError, MongoOperationWithoutAffectError


logger = logging.getLogger("")


async def edit_event_object(event_to_update: dict):
    """Edits Event object in database.

    Parameters
    ----------
    event_to_update : Event
        Object represents an event saved in database.
        To see more, check `app/models/api.py`.

    Raises
    ------
    RuntimeError
        Out of fuel

    Returns
    -------
    None
    """
    mongo_client = Mongo()
    result = mongo_client.edit_record(Event(**event_to_update))

    if result.matched_count == 0:
        msg = "Specified object wasn't found for `edit` operation."
        logger.warning(msg)
        raise MongoNotFoundError(msg)
    if result.modified_count == 0:
        msg = "Specified object wasn't updated, operation was ignored."
        logger.warning(msg)
        raise MongoOperationWithoutAffectError(msg)

    logger.info("Event was successfully edited.")


