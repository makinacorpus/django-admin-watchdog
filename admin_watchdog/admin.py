from django.contrib import admin
from django.utils.html import format_html
from django.utils.translation import ugettext_lazy as _

from admin_watchdog.models import LogEntry


class LogEntryAdmin(admin.ModelAdmin):
    class Media:
        css = {
            'all': ['admin_watchdog/admin.css']
        }

    date_hierarchy = 'when'
    list_display = ('when', 'levelname', 'shortmessage')
    list_filter = ('levelname',)
    readonly_fields = (
        'when', 'levelname', 'shortmessage',
        'show_message', 'show_request_repr'
    )
    search_fields = (
        'shortmessage', 'message', 'request_repr',
    )

    def show_message(self, instance):
        return format_html('<pre>{0}</pre>', instance.message)
    show_message.short_description = _('Message')
    show_message.allow_tags = True

    def show_request_repr(self, instance):
        return format_html('<pre>{0}</pre>', instance.request_repr)
    show_request_repr.short_description = _('Request representation')
    show_request_repr.allow_tags = True


admin.site.register(LogEntry, LogEntryAdmin)
