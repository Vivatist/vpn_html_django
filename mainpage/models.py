from django.db import models


class Links(models.Model):
    '''Содержит внешние ссылки используемые на сайте'''
    name = models.CharField(max_length=50, db_index=True)
    url = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name
