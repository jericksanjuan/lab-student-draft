try:
    from django.conf.urls import *
except ImportError:  # django < 1.4
    from django.conf.urls.defaults import *
from . import views

urlpatterns = patterns(
    "",
    url(r'^rank-preference/(?P<pk>\d+)/$', views.rank_preference, name="rank-preference"),
    url(r'^update-group/(?P<pk>\d+)/$', views.update_group, name="update-group"),
)
