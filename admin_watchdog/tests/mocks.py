from django.http.request import QueryDict


class RequestMock(object):
    path = "/"
    GET = QueryDict('')
    POST = QueryDict('')
    COOKIES = {}
    _post_parse_error = False


class RecordMock(object):
    def __init__(self, request):
        if request is not None:
            self.request = request
        self.levelname = "ERROR"
        self.exc_info = (None, AttributeError(), None)
        self.exc_text = None
        self.stack_info = False

    def getMessage(self):
        return "Short Message Mock"
