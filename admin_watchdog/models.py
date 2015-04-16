from django.db import models
from django.utils.translation import ugettext_lazy as _


class LogEntry(models.Model):
    class Meta:
        verbose_name = _("Log entry")
        verbose_name_plural = _("Log entries")
        app_label = "admin_watchdog"

    when = models.DateTimeField(
        _("When"),
        auto_now_add=True,
        editable=False,
    )
    levelname = models.CharField(
        _("Level name"),
        max_length=20,
        editable=False,
    )
    shortmessage = models.CharField(
        _("Short message"),
        max_length=256,
        editable=False,
    )
    message = models.TextField(
        _("Message"),
        editable=False,
    )
    request_repr = models.TextField(
        _("Request representation"),
        editable=False,
    )
