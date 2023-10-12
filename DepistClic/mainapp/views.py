from django.shortcuts import render
from .models import Question
from django.http import JsonResponse


# Create your views here.
def home(request):
    return render(request, 'mainapp/home.html')


def questions(request):
    first_question = Question.objects.first()
    context = {
        'question': first_question
    }
    return render(request, 'mainapp/questions.html', context)


def get_question(request, question_id):
    question = Question.objects.get(pk=question_id)
    context = {
        'question': question
    }
    return render(request, 'mainapp/questions.html', context)


def synthese(request):
    return render(request, 'mainapp/synthese.html')
