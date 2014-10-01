from django.conf.urls import patterns, include, url
from django.contrib import admin


def test_view(request):
    raise AttributeError()


urlpatterns = patterns(
    '',

    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', test_view)
)
