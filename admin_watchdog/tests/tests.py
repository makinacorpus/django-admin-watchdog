from django.test import Client, TestCase
from django.contrib.auth.models import User

from admin_watchdog.handlers import AdminWatchdogHandler
from admin_watchdog.models import LogEntry
from admin_watchdog.tests import mocks


class ModelTestCase(TestCase):
    def test_object_creation(self):
        """ Test a simple log entry creation. """
        LogEntry.objects.create(
            levelname="DEBUG",
            shortmessage="shortmessage",
            message="longer message.",
            request_repr="request",
        )
        log = LogEntry.objects.last()
        self.assertEqual(LogEntry.objects.all().count(), 1)
        self.assertEqual(log.levelname, "DEBUG")
        self.assertTrue(log.when)


class HandlerTestCase(TestCase):
    def setUp(self):
        self.handler = AdminWatchdogHandler()

    def test_emit_with_request(self):
        request = mocks.RequestMock()
        record = mocks.RecordMock(request)
        self.handler.emit(record)
        self.assertEqual(LogEntry.objects.all().count(), 1)
        log = LogEntry.objects.last()
        self.assertEqual(log.levelname, u'ERROR')
        self.assertNotEqual(log.request_repr, u'unavailable')

    def test_emit_without_request(self):
        record = mocks.RecordMock(None)
        self.handler.emit(record)
        self.assertEqual(LogEntry.objects.all().count(), 1)
        log = LogEntry.objects.last()
        self.assertEqual(log.levelname, u'ERROR')
        self.assertEqual(log.request_repr, u'unavailable')


class FunctionalTestCase(TestCase):
    def setUp(self):
        self.logentry = LogEntry.objects.create(
            levelname="DEBUG123",
            shortmessage="shortmessage123",
            message="longer message. 123",
            request_repr="request123",
        )
        user = User.objects.create_superuser('admin', '', 'password')
        self.c = Client()
        self.c.force_login(user)

    def test_log_entries_list_view(self):
        """ Test the admin view listing all log entries. """
        response = self.c.get('/admin/admin_watchdog/logentry/')
        self.assertEqual(response.status_code, 200)
        self.assertIn("DEBUG123", response.content.decode('utf8'))
        self.assertIn("shortmessage123", response.content.decode('utf8'))
        self.assertNotIn(
            "longer message. 123",
            response.content.decode('utf8')
        )
        self.assertNotIn("request123", response.content.decode('utf8'))

    def test_log_entry_view(self):
        """ Test the admin view listing a single log entry. """
        response = self.c.get('/admin/admin_watchdog/logentry/{}/change/'.format(self.logentry.pk), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn("DEBUG123", response.content.decode('utf8'))
        self.assertIn("shortmessage123", response.content.decode('utf8'))
        self.assertIn("longer message. 123", response.content.decode('utf8'))
        self.assertIn("request123", response.content.decode('utf8'))

    def test_error_page(self):
        """ Test a page raising an error. A log entry should be created. """
        self.assertRaises(AttributeError, self.c.get, '/')
        self.assertEqual(LogEntry.objects.all().count(), 2)
        log = LogEntry.objects.last()
        self.assertEqual(log.levelname, u'ERROR')
        self.assertEqual(log.shortmessage, u'Internal Server Error: /')
