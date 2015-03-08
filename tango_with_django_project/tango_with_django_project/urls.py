from django.conf.urls import patterns, include, url
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.conf import settings
from registration.backends.simple.views import RegistrationView


class MyRegistrationView(RegistrationView):
    def get_success_url(self,request, user):
        return '/rango/add_profile'

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tango_with_django_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^rango/', include('rango.urls')),
    url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),
    (r'^accounts/', include('registration.backends.simple.urls')),

    #url(r'^password/change/$', 'django.contrib.auth_views.password_change', name = 'password_change'),
    #url(r'^password/change/$', auth_views.password_change, name='password_change'),
    #url(r'^password/change/done/$', auth_views.password_change_done, name='password_change_done'),
)

if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'^media/(?P<path>.*)',
         "serve",
        {'document_root': settings.MEDIA_ROOT}), )
