from django.db import models
from prose.fields import RichTextField


class Page(models.Model):
    title = models.CharField(max_length=200)
    content = models.JSONField(default=dict)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
