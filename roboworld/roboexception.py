class RoboException(Exception):
    pass


class WallInFrontException(RoboException):
    pass


class ObjectMissingException(RoboException):
    pass


class ObjectIsHereException(RoboException):
    pass


class SpaceIsFullException(RoboException):
    pass


class SpaceIsEmptyException(RoboException):
    pass
