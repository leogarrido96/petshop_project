from django.urls import path

from .views import GalleryView, PhotoUploadView, photo_action

app_name = 'gallery'

urlpatterns = [
    path('', GalleryView.as_view(), name='gallery_list'),
    path('upload/', PhotoUploadView.as_view(), name='photo_upload'),
    path('foto/<int:pk>/<str:action>/', photo_action, name='photo_action')
]
