from django.conf.urls import url
from .views import ReviewList

urlpatterns = [
    url(r'^$', ReviewList.as_view(), name='list'),
]
