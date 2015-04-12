from django.conf.urls import include, url
from django.contrib import admin
from taleggio.views import auth_test

urlpatterns = [
    # Examples:
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'taleggio.views.index', name='index'),
    url(r'^dwelling/', include('dwelling.urls')),
    url(r'^auth_test/$', 'taleggio.views.auth_test', name='auth_test'),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url('', include('django.contrib.auth.urls', namespace='auth')),

    url(r'^admin/', include(admin.site.urls)),
]

# Remove from production and serve staticfiles via Nginx
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()
