from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)  # также удалит записи связанные со вторичной таблицей
    title = models.CharField(max_length=200, unique=True)
    text = models.TextField()
    published_date = models.DateTimeField(blank=True, null=True)  # поле не обязательно и мб пустым
    created_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title  # получим строку с заголовком

    # def approved_comments(self):
    #     return self.comments.filter(approved_comment=True)