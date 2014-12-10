try:
    from django.conf.urls import *
except ImportError:  # django < 1.4
    from django.conf.urls.defaults import *
from . import views

urlpatterns = patterns(
    "",
    url(r'^select-group/$', views.select_group, name="select-group"),
)
