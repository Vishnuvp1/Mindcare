from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', include('user.urls')),
    path('psychologist/', include('psychologist.urls')),
    path('chat/', include('chat.urls')),
    path('adminpanel/', include('adminpanel.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
