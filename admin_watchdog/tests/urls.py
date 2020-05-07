from django.contrib import admin


def test_view(request):
    raise AttributeError()


try:
    # Django >= 2.0
    from django.urls import path

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', test_view),
    ]
except ImportError:
    # Django >= 1.10
    from django.conf.urls import url, include

    urlpatterns = [
        url(r'^admin/', include(admin.site.urls)),
        url(r'^$', test_view),
    ]
