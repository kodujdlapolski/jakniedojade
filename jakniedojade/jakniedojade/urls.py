from django.conf.urls import include, url
from django.conf import settings
from django.contrib import admin
from app.routes import router
from app.views import AddVoteView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/connections/(?P<connection_id>[0-9]+)/vote', AddVoteView.as_view()),
    url(r'^api/', include(router.urls)),
]
if settings.DEBUG is True:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
        url(r'^$', 'django.views.static.serve', {'path': 'index.html', 'document_root': settings.STATIC_ROOT}),
    ]

