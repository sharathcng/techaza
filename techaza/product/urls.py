from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('product', views.ProductsList.as_view(), name='product'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
