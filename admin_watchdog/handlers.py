import logging

from django.views.debug import ExceptionReporter, get_exception_reporter_filter

from admin_watchdog.models import LogEntry


class AdminWatchdogHandler(logging.Handler):
    """An exception log handler that register exception for the site backend.
    """

    def __init__(self):
        logging.Handler.__init__(self)

    def emit(self, record):
        # Get request specific info (location, ...)
        try:
            request = record.request
            filter = get_exception_reporter_filter(request)
            request_repr = filter.get_request_repr(request)
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

