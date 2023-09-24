from django.shortcuts import render
from .models import Links, Settings


def get_client_ip(req):
    """Возвращает ip-адрес посетиителя сайта"""
    x_forwarded_for = req.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[0]
    else:
        ip = req.META.get("REMOTE_ADDR")
    return ip


def index(request):
    context = {
        "settings": Settings.objects.get(lang="ru"),
    }

    ip_addr = get_client_ip(request)
    check = ip_addr == context["settings"].host
    print("IP:", ip_addr, " Check:", check)

    return render(request, "mainpage/index.html", context=context)
