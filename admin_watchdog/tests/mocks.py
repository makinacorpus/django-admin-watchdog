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
        self.exc_info = (None, self.getMessage(), None)
        self.exc_text = ""

    def getMessage(self):
        return "Short Message Mock"
