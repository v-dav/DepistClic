from django.shortcuts import render
from .models import Question


# Create your views here.
def home(request):
    return render(request, 'mainapp/home.html')


def questions(request):
    first_question = Question.objects.get(pk=2)
    context = {
        'first_question': first_question
    }
    return render(request, 'mainapp/questions.html', context)


def synthese(request):
    return render(request, 'mainapp/synthese.html')
