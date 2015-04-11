from django.conf.urls import url
from dwellings.views import DwellingList, DwellingView, DwellingCreate, DwellingDelete

urlpatterns = [
    url(r'^create$/', DwellingCreate.as_view(), name='crete'),
    url(r'^(?P<id>)$', DwellingView.as_view(), name='detail'),
    url(r'^(?P<id>)/edit$', DwellingUpdate.as_view(), name='update'),
    url(r'^(?P<id>)/delete$', DwellingDelete.as_view(), name='delete'),
    url(r'^$', DwellingList.as_view(), name='list'),
]
