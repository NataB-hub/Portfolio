from django.db import models
from django.conf import settings


class Blog(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # также удалит записи связанные со
    # вторичной таблицей
    title = models.CharField(max_length=200, unique=True)
    text = models.TextField()
    published_date = models.DateTimeField(blank=True, null=True)
    url = models.URLField(blank=True)
    ref_name = models.CharField(blank=True, null=True, max_length=50)

    def __str__(self):
        return self.title  # получим строку с заголовком
