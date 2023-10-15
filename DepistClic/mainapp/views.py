from django.shortcuts import render
from .models import Question, Answer
from django.http import JsonResponse
from .forms import AnswerForm


# Create your views here.
def home(request):
    return render(request, 'mainapp/home.html')


def get_question(request, question_order=None):
    query_set = Answer.objects.all()

    if question_order is None:
        question = Question.objects.first()
    else:
        question = Question.objects.get(order=question_order)

    form = AnswerForm(request.POST or None, initial={'question': question.id})
    if form.is_valid():
        form.save()
        form = AnswerForm(initial={'question': question.id})

    context = {
        'question': question,
        'answer_list': query_set,
        'form': form,
    }

    return render(request, 'mainapp/questions.html', context)


def synthese(request):
    return render(request, 'mainapp/synthese.html')
