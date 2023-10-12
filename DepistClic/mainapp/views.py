from django.shortcuts import render
from .models import Question
from django.http import JsonResponse


# Create your views here.
def home(request):
    return render(request, 'mainapp/home.html')


def get_question(request, question_id=None):
    if question_id is None:
        question = Question.objects.first()
    else:
        question = Question.objects.get(pk=question_id)
    context = {
        'question': question
    }
    return render(request, 'mainapp/questions.html', context)


def synthese(request):
    return render(request, 'mainapp/synthese.html')
