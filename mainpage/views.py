from django.shortcuts import render
from mainpage.links import Links
from .models import *


def get_client_ip(req):
    """Возвращает ip-адрес посетиителя сайта"""
    x_forwarded_for = req.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[0]
    else:
        ip = req.META.get("REMOTE_ADDR")
    return ip


def index(request):
    class Settings:
        url = "http://sssvpn.ru"
        url_support = "https://t.me/+hU9vIxKbtwg3ZGI6"
        # host = "127.0.0.1"
        host = "5.104.108.237"
        port = "14983"
        password = "238938"
        encription = "AES-256-GCM"
        ss_link = "ss://YWVzLTI1Ni1nY206MjM4OTM4@5.104.108.237:14983/#sssvpn.ru"
        links = Links.objects

    ip_addr = get_client_ip(request)
    check = ip_addr == Settings.host
    print("IP:", ip_addr, " Check:", check)

    return render(request, "index.html", {"settings": Settings, "links": Links})
