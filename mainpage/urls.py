from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='home'),
    path("update_ip/", views.update_ip, name='update_ip'),
]
