.PHONY: test coverage

test:
	DJANGO_SETTINGS_MODULE=admin_watchdog.tests.settings django-admin.py test admin_watchdog.tests

coverage:
	DJANGO_SETTINGS_MODULE=admin_watchdog.tests.settings coverage run `which django-admin.py` test admin_watchdog.tests
	coverage html
