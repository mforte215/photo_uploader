from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),                
  path('upload/', views.upload_photo, name='upload'),
  path('gallery/', views.view_gallery, name='gallery'),
]
