from django.db import models


class Question(models.Model):
    title = models.TextField(max_length=200)
    response_type = models.CharField(max_length=50)
    order = models.PositiveIntegerField()
    display_text = models.TextField(max_length=50, default='Texte')

    def __str__(self):
        return self.title


class Comment(models.Model):
    comment_area = models.TextField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment_area


class ScreeningTest(models.Model):
    SYSTÉMATIQUE = 'Systématique'
    CONDITIONNEL = 'Conditionnel'

    TYPE_CHOICES = [
        (SYSTÉMATIQUE, 'Systématique'),
        (CONDITIONNEL, 'Conditionnel'),
    ]

    title = models.TextField(max_length=200)
    frequency = models.CharField(max_length=50)
    sources = models.JSONField(blank=True, null=True, default=list)
    info = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    ordo = models.FileField(upload_to='ordonnances/', blank=True, null=True)

    type = models.CharField(
        max_length=15,
        choices=TYPE_CHOICES,
        default=SYSTÉMATIQUE,  # Choix par défaut
    )
    
    def get_ordo_url(self):
        if self.ordo:
            return self.ordo.url
        return None

    def __str__(self):
        return self.title
