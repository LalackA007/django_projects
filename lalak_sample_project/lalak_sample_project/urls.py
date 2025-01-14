from django.contrib import admin
from django.urls import include, path
<<<<<<< HEAD
from django.conf import settings
from django.conf.urls.static import static
=======
>>>>>>> 00c691414f1328b5762828267d913cdb8ad70007

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("home_app.urls")),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('blog_app.urls')),
<<<<<<< HEAD
    path('social-auth/', include('social_django.urls', namespace='social')),
    path('images/', include('bookmarks_app.urls', namespace='images'))
]

if settings.DEBUG:
    urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)
=======
]
>>>>>>> 00c691414f1328b5762828267d913cdb8ad70007
