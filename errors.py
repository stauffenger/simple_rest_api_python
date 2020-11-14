class BadRequest(Exception):
    def __init__(self, message):
        self.title = "Bad Request"
        self.message = message
        super().__init__(self.message)

class InternalServerError(Exception):
    def __init__(self, message):
        self.title = "Internal Server Error"
        self.message = message
        super().__init__(self.message)

class NotFound(Exception):
    def __init__(self, message):
        self.title = "Not Found"
        self.message = message
        super().__init__(self.message)
