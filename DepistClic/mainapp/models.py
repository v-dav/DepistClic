from django.db import models


# Create your models here.
class Question(models.Model):
    title = models.TextField()
    response_type = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.TextField()

    def __str__(self):
        return self.answer_text
