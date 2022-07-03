class MongoError(Exception):
    """Generic Mongo related error."""
    pass


class MongoNotFoundError(MongoError):
    """Error for cases, when specified object wasn't found in database."""
    pass


class MongoOperationWithoutAffectError(MongoError):
    """Error for cases, when specified operation was ignored or brought no affect (ignored)."""
    pass
