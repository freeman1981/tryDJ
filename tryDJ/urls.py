from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'tryDJ.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),
                       url(r'^polls/', include('polls.urls', namespace="polls")),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^quiz/', include('mdls.urls')),
                       url(r'^mdls/', include('mdls.urls')),
                       )

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
