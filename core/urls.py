from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers


from catalog.views import ProductViewSet, CategoryViewSet
from gallery.views import PhotoViewSet
from main.views import SiteConfigViewSet, ContactMessageViewSet

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'gallery', PhotoViewSet)
router.register(r'site-config', SiteConfigViewSet)
router.register(r'contact', ContactMessageViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),

    # Rotas dos Apps
    path('', include('main.urls')),
    path('catalogo/', include('catalog.urls')),
    path('galeria/', include('gallery.urls')),

    # Rota da API
    path('api/v1/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]

# Configuração para servir imagens no modo DEBUG (Desenvolvimento)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
