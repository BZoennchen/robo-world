class RoboException(Exception):
    def __init__(self, message=""):
        self.message = message
        super().__init__(self.message)


class InvalidWorldArgumentsExeception(Exception):
    def __init__(self, message="Invalid world arguments."):
        self.message = message
        super().__init__(self.message)


class WallInFrontException(RoboException):
    def __init__(self, message="There is a wall in front."):
        self.message = message
        super().__init__(self.message)


class ObjectMissingException(RoboException):
    def __init__(self, message="There is no object that can be taken."):
        self.message = message
        super().__init__(self.message)


class ObjectIsHereException(RoboException):
    def __init__(self, message="The space is occupied by an object."):
        self.message = message
        super().__init__(self.message)


class SpaceIsFullException(RoboException):
    def __init__(self, message="The space is occupied by something."):
        self.message = message
        super().__init__(self.message)


class SpaceIsEmptyException(RoboException):
    def __init__(self, message="There is nothing to pick up."):
        self.message = message
        super().__init__(self.message)
