from django.conf.urls import url
from .views import DwellingList, DwellingView, DwellingCreate, DwellingDelete,\
    DwellingUpdate


urlpatterns = [
    url(r'^create$/', DwellingCreate.as_view(), name='crete'),
    url(r'^(?P<pk>\d+)/$', DwellingView.as_view(), name='detail'),
    url(r'^(?P<id>)/edit$', DwellingUpdate.as_view(), name='update'),
    url(r'^(?P<id>)/delete$', DwellingDelete.as_view(), name='delete'),
    url(r'^$', DwellingList.as_view(), name='list'),
]
