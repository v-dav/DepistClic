from django.shortcuts import render
from .models import Question, Answer
from django.http import JsonResponse


# Create your views here.
def home(request):
    return render(request, 'mainapp/home.html')

from .models import Answer

def store_value(request):
    if request.method == 'POST':
        # Get the user answer from the POST request
        user_answer = request.POST.get('user_answer')
        
        # Get the current question
        current_question = Question.objects.first()
        
        # Create a new Answer instance and save it to the database
        answer = Answer(answer_text=user_answer, question=current_question)
        answer.save()
        
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False, 'error': 'Methode de requete non valide'})

def get_question(request, question_id=None):
    query_set = Answer.objects.all()
    
    if question_id is None:
        question = Question.objects.first()
    else:
        question = Question.objects.get(pk=question_id)
    context = {
        'question': question,
        'answer_list': query_set
    }
    return render(request, 'mainapp/questions.html', context)


def synthese(request):
    return render(request, 'mainapp/synthese.html')
