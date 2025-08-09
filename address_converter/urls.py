# address_converter/urls.py (새 파일)
from django.urls import path
from . import views

urlpatterns = [
    path('', views.address_converter_view, name='address_converter_view'),
]