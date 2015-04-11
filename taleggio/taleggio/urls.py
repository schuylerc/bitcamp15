from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'taleggio.views.index', name='index'),
    url(r'^dwellings/$', 'dwelling.views.dwellings', name='dwellings'),
    url(r'^dwelling/(?P<dwelling_id>\d+)/$', 'dwelling.views.dwellingDetail', name='dwellingDetail'),
    url(r'^reviews/$', 'review.views.reviews', name='reviews'),
    url(r'^review/(?P<review_id>\d+)/$', 'review.views.reviewDetail', name='reviewDetail'),
    url(r'^auth_test/$', 'taleggio.views.auth_test', name='auth_test'),
    url(r'^auth_test/$', 'taleggio.views.auth_test', name='auth_test'),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url('', include('django.contrib.auth.urls', namespace='auth')),

    url(r'^admin/', include(admin.site.urls)),
]

# Remove from production and serve staticfiles via Nginx
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()
