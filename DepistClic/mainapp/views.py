from django.shortcuts import render, redirect
from .models import Question


# Create your views here.
def home(request):
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
    return render(request, 'mainapp/questions.html', context)


def synthese(request):
    return render(request, 'mainapp/synthese.html')
