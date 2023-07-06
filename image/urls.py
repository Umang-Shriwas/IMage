from django.urls import path
from .views import *

urlpatterns = [
    path('add_images', ImagesAPI.as_view(), name='add_images'),
    path('gets_all_images', ImagesAPI.as_view(), name='gets_all_images'),
    path('get_images/<int:pk>',ImagesAPI.as_view(), name='get_images'),
    path('update_images/<int:pk>', ImagesAPI.as_view(), name='update_images'),
    path('delete_images/<int:pk>', ImagesAPI.as_view(), name='delete_images'),
]
