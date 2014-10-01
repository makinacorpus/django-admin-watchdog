from django.db import models


class LogEntry(models.Model):
    class Meta:
        verbose_name_plural = "LogEntries"

    when = models.DateTimeField(
        "When",
        auto_now_add=True,
        editable=False,
    )
    levelname = models.CharField(
        "Level name",
        max_length=20,
        editable=False,
    )
    shortmessage = models.CharField(
        "Short message",
        max_length=256,
        editable=False,
    )
    message = models.TextField(
        "Message",
        editable=False,
    )
    request_repr = models.TextField(
        "Request representation",
        editable=False,
    )
