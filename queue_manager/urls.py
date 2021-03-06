from django.contrib import admin
from django.urls import path, include


from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('orders.urls')),
    path('api/', include('kitchens.urls')),
    path('api/', include('accounts.urls')),
    path('api/', include('branches.urls')),
    path('api/', include('informations.urls')),
]


urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)