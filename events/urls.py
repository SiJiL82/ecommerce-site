from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_events, name='events'),
    path('remove/<eventid>/', views.remove_event, name='remove_event'),
]
