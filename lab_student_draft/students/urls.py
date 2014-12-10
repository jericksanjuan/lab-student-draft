try:
    from django.conf.urls import *
except ImportError:  # django < 1.4
    from django.conf.urls.defaults import *
from . import views

urlpatterns = patterns(
    "",
    url(r'^rank-preference/$', views.rank_preference, name="rank-preference"),
    url(r'^update-group/$', views.update_group, name="update-group"),
)
