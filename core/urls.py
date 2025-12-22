from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Configuração da API (Router)
from rest_framework import routers
# Vamos importar as Views da API depois que criarmos, por enquanto deixe comentado se der erro
# from catalog.views import ProductViewSet
# from gallery.views import PhotoViewSet

router = routers.DefaultRouter()
# router.register(r'produtos', ProductViewSet)
# router.register(r'galeria', PhotoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),

    # Rotas dos Apps
    path('', include('main.urls')),  # A Home fica no app main
    path('catalogo/', include('catalog.urls')),
    path('galeria/', include('gallery.urls')),

    # Rota da API
    path('api/', include(router.urls)),
]

# Configuração para servir imagens no modo DEBUG (Desenvolvimento)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
