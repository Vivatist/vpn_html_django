from django.db import models


class Links(models.Model):
    """Содержит внешние ссылки используемые на сайте"""

    class Meta:
        verbose_name = "Внешние ссылки"
        verbose_name_plural = "Внешние ссылки"
        ordering = ["name"]

    name = models.CharField(max_length=50, db_index=True, verbose_name='Название')
    url = models.CharField(max_length=200, verbose_name='URL')

    def __str__(self) -> str:
        return self.name
