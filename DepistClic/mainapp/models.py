from django.db import models


class Question(models.Model):
    title = models.TextField(max_length=200)
    response_type = models.CharField(max_length=50)
    order = models.PositiveIntegerField()
    display_text = models.TextField(max_length=50, default='Texte')

    def __str__(self):
        return self.title
