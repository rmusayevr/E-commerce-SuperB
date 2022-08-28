from django.conf import settings
from django.contrib import admin
from django.urls import path, include 
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Blog.urls')),
    path('', include('Core.urls')),
    path('', include('Order.urls')),
    path('', include('User.urls')),
    path('', include('Product.urls')),
    path('', include('social_django.urls', namespace='social')),
    path('api/', include('Product.api.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
] 
urlpatterns +=  static(settings.STATIC_URL, document_root = settings.STATIC_ROOT) 
urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
