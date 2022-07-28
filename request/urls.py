from django.urls import path
from . import views

urlpatterns = [
    path('', views.request, name='request'),
    path('remove/<requestid>/', views.remove_request, name='remove_request'),
    path('update/<requestid>/', views.update_request, name='update_request')
]
