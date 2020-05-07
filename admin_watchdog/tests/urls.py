from django.contrib import admin
from django.urls import path


def test_view(request):
    raise AttributeError()


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', test_view),
]
