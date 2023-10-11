from django.shortcuts import render
from .models import Question
from django.http import JsonResponse


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


def get_question(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
        data = {
            'title': question.title,
            'response_type': question.response_type,
        }
        return JsonResponse(data)
    except Question.DoesNotExist:
        return JsonResponse({'error': "La question n'existe pas"}, status=404)
