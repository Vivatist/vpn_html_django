from django.urls import path
from vpn import views

urlpatterns = [
    path("", views.home, name="home"),
]
