from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'lolcomp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'admin/', include('editor.urls')),
    url(r'', include('compselector.urls')),
    url(r'^admin2/', include(admin.site.urls)),
)
