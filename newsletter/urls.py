from django.urls import path
from . import views

urlpatterns = [
    path('', views.signup, name='newsletter_signup')
]
