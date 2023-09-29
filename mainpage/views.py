from django.shortcuts import render
from .models import Settings, BlockedSites, Clients
from django.http import JsonResponse, HttpResponseNotFound


def get_ip(req):
    """Возвращает ip-адрес отправителя запроса сайта"""
    x_forwarded_for = req.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[0]
    else:
        ip = req.META.get("REMOTE_ADDR")
    return ip


def update_ip(request):
    def is_ajax():
        return request.headers.get("x-requested-with") == "XMLHttpRequest"

    """Обрабатывает AJAX запросы и возвращает ip"""
    if is_ajax():
        data = {"ip": get_ip(request)}
        return JsonResponse(data)
    else:
        # Обычный HTTP-запрос - возвращаем ошибку
        print("Запрос ip")
        return HttpResponseNotFound("Неверный формат запроса. Ожидается AJAX.")  


# HttpResponseNotFound


def index(request):
    """Главная страница"""
    context = {
        "settings": Settings.objects.get(lang="ru"),
        "blocked_sites": BlockedSites.objects.all(),
        "clients": Clients.objects.all(),
    }

    ip_addr = get_ip(request)
    check = ip_addr == context["settings"].host
    print("IP:", ip_addr, " Check:", check)

    context["client_ip"] = ip_addr
    context["check_ip"] = check

    return render(request, "mainpage/index.html", context=context)
