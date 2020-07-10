import logging
from pprint import pformat

from django.utils.encoding import force_str


def build_request_repr(request):
    """
    FROM Django 1.8

    Builds and returns the request's representation string. The request's
    attributes may be overridden by pre-processed values.
    """
    # Since this is called as part of error handling, we need to be very
    # robust against potentially malformed input.
    try:
        get = pformat(request.GET)
    except Exception:
        get = '<could not parse>'
    try:
        post = pformat(request.POST)
    except Exception:
        post = '<could not parse>'
    try:
        cookies = pformat(request.COOKIES)
    except Exception:
        cookies = '<could not parse>'
    try:
        meta = pformat(request.META)
    except Exception:
        meta = '<could not parse>'
    return force_str('<%s\npath:%s,\nGET:%s,\nPOST:%s,\nCOOKIES:%s,\nMETA:%s>' %
                     (request.__class__.__name__,
                      request.path,
                      str(get),
                      str(post),
                      str(cookies),
                      str(meta)))


class AdminWatchdogHandler(logging.Handler):
    """An exception log handler that register exception for the site backend.
    """

    def __init__(self):
        logging.Handler.__init__(self)

    def emit(self, record):
        from admin_watchdog.models import LogEntry

        # Get request specific info (location, ...)
        try:
            request = record.request
            request_repr = build_request_repr(request)
        except AttributeError:
            request = None
            request_repr = u"unavailable"

        LogEntry(
            levelname=record.levelname,
            shortmessage=record.getMessage(),
            message=self.format(record),
            request_repr=request_repr,
        ).save()

        # May be used for more advanced logging
        """
        # Get ExceptionReporter parameters
        if record.exc_info:
            exc_info = record.exc_info
        else:
            exc_info = (None, record.getMessage(), None)


        message = "%s\n\nRequest repr(): %s" % (
            self.format(record), request_repr
        )
        reporter = ExceptionReporter(request, is_email=True, *exc_info)
        html_message = reporter.get_traceback_html()
        text_message = reporter.get_traceback_text()
        """
