from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

urlpatterns = [
    path('', include('Blog.urls')),
    path('', include('Core.urls')),
    path('', include('Order.urls')),
    path('', include('User.urls')),
    path('', include('Product.urls')),
    path('', include('social_django.urls', namespace='social')),
    path('api/', include('api.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
] 

urlpatterns += i18n_patterns (
    path('admin/', admin.site.urls),
    path('', include('Core.urls'))
)

urlpatterns +=  static(settings.STATIC_URL, document_root = settings.STATIC_ROOT) 
urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += [
        re_path(r'^rosetta/', include('rosetta.urls'))
    ]
