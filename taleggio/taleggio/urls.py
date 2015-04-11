from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'taleggio.views.index', name='index'),
    url(r'^login/$', 'taleggio.views.login', name='login'),
    url(r'^dwelling/$', 'taleggio.views.dwelling', name='dwelling'),
    #url('', include('social.apps.django_app.urls', namespace='social')),

    url(r'^admin/', include(admin.site.urls)),
]

# Remove from production and serve staticfiles via Nginx
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()
