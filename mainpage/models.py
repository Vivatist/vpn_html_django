from django.db import models
from django.urls import reverse


class Settings(models.Model):
    """Глобальные настройка приложения"""

    class Meta:
        verbose_name = "Глобальные настройки"
        verbose_name_plural = "Глобальные настройки"
        ordering = ["lang"]

    lang = models.CharField(max_length=2, verbose_name="Язык")
    url = models.URLField(verbose_name="Ссылка на сайт")
    host = models.GenericIPAddressField(default='127.0.0.1', verbose_name="IP хоста")
    url_support = models.URLField(verbose_name="URL телеграм-канала техподдержки")
    key = models.CharField(max_length=100, verbose_name="Ключ")

    def __str__(self) -> str:
        return self.lang


class BlockedSites(models.Model):
    """Список заблокированных сайтов"""

    class Meta:
        verbose_name = "Заблокированный сайт"
        verbose_name_plural = "Заблокированные сайты"
        ordering = ["name"]

    name = models.CharField(max_length=50, verbose_name="Название")
    url = models.URLField(verbose_name="URL заблокированного ресурса")
    description = models.TextField(verbose_name="Описание")
    favicon = models.ImageField(upload_to="upload/", verbose_name="Иконка 16x16")
    active = models.BooleanField(default=True, verbose_name="Активно")

    def __str__(self) -> str:
        return self.name


class Clients(models.Model):
    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"

    name = models.CharField(verbose_name="Название", max_length=50)
    url = models.URLField(verbose_name="Ссылка на скачивание", max_length=200)
    logo = models.ImageField(verbose_name="Логотип клиента", upload_to="upload/")
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Downloads_detail", kwargs={"pk": self.pk})
