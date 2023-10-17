from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, JsonResponse
from .models import Question


# Create your views here.
def home(request):
    request.session.clear()
    return render(request, 'mainapp/home.html')


def get_question(request, question_order=None):
    if request.method == 'POST':
        # Get the user answer and question order from the POST request
        user_answer = request.POST.get('user_answer')
        q_order = request.POST.get('question_order')
        next_question_order = int(q_order) + 1

        # Store the answer in the session
        request.session[f'q{q_order}'] = user_answer

        # Redirect to the next question 
        return redirect('depistclic-get_question', question_order=next_question_order)

    # Get the question for the GET request
    if question_order is None:
        question = Question.objects.first()
        context = {
            'question': question
            }
    else:
        question = Question.objects.get(order=question_order)
        previous_answers = []
        for i in range(1, question_order):
            answer_key = f'q{i}'
            previous_answer = request.session.get(answer_key)
            previous_answers.append(previous_answer)
        context = {
            'question': question,
            'previous_answers': previous_answers,
        }
    
    if is_last_question(question_order, total_questions=10):
        return HttpResponseRedirect('/synthese/')
    
    return render(request, 'mainapp/questions.html', context)

def is_last_question(question_order, total_questions=10):
    return question_order == total_questions

def synthese(request):
    previous_answers = []
    for i in range(1, 11):
        answer_key = f'q{i}'
        previous_answer = request.session.get(answer_key)
        if previous_answer:
            previous_answers.append(previous_answer)
    
    context = {
        'previous_answers': previous_answers,
    }
    
    return render(request, 'mainapp/synthese.html', context)
