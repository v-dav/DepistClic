from django.db import models


class Question(models.Model):
    title = models.TextField()
    response_type = models.CharField(max_length=50)
    order = models.PositiveIntegerField()

    def __str__(self):
        return self.title
