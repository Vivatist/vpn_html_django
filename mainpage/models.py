from django.db import models


class Links(models.Model):
    """Внешние ссылки используемые на сайте"""

    class Meta:
        verbose_name = "Внешние ссылки"
        verbose_name_plural = "Внешние ссылки"
        ordering = ["name"]

    name = models.CharField(max_length=50, db_index=True, verbose_name="Название")
    url = models.CharField(max_length=200, verbose_name="URL")

    def __str__(self) -> str:
        return self.name


class Settings(models.Model):
    """Глобальные настройка приложения"""

    class Meta:
        verbose_name = "Глобальные настройки"
        verbose_name_plural = "Глобальные настройки"
        ordering = ["lang"]

    lang = models.CharField(max_length=2, verbose_name="Язык")
    url = models.URLField(verbose_name="Ссылка на сайт")
    url_support = models.URLField(verbose_name="URL телеграм-канала техподдержки")
    host = models.GenericIPAddressField(verbose_name="IP хоста")
    port = models.IntegerField(verbose_name="Порт сервера")
    password = models.CharField(max_length=20, verbose_name="Парль сервера")
    encription = models.CharField(max_length=20, verbose_name="Тип шифрования")
    key = models.CharField(max_length=100, verbose_name="Ключ")
    android_client = models.URLField(verbose_name="Ссылка на клиент для Android")
    windows_client = models.URLField(verbose_name="Ссылка на клиент для Windows")
    ios_client = models.URLField(verbose_name="Ссылка на клиент для iOS")
    macos_client = models.URLField(verbose_name="Ссылка на клиент для MacOS")
    chrome_client = models.URLField(verbose_name="Ссылка на клиент для Chrome")
    linux_client = models.URLField(verbose_name="Ссылка на клиент для Linux")

    def __str__(self) -> str:
        return self.lang


class BlockedSites(models.Model):
    """Список заблокированных сайтов"""

    class Meta:
        verbose_name = "Заблокированные сайты"
        verbose_name_plural = "Заблокированные сайты"
        ordering = ["name"]

    name = models.CharField(max_length=50, verbose_name="Название")
    url = models.URLField(verbose_name="URL заблокированного ресурса")
    description = models.TextField(verbose_name="Описание")
    favicon = models.ImageField(
        upload_to="upload/", verbose_name="Иконка"
    )
    active = models.BooleanField(default=True, verbose_name="Активно")

    def __str__(self) -> str:
        return self.name
