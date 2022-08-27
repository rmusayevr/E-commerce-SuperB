from django.conf import settings
from django.contrib import admin
from django.urls import path, include 
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Blog.urls')),
    path('', include('Core.urls')),
    path('', include('Order.urls')),
    path('', include('User.urls')),
    path('', include('Product.urls')),
    path('api/', include('Product.api.urls')),
    path('', include('social_django.urls', namespace='social'))
] 
urlpatterns +=  static(settings.STATIC_URL, document_root = settings.STATIC_ROOT) 
urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
