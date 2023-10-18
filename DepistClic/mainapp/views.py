from django.shortcuts import render, redirect
from .models import Question


# Homepage view
def home(request):
    request.session.clear()
    return render(request, 'mainapp/home.html')


# The view that stores the answer in a session and gets a question
def get_question(request, question_order=None):
    if request.method == 'POST':
        user_answer = request.POST.get('user_answer')
        q_order = request.POST.get('question_order')
        next_question_order = int(q_order) + 1

        # Store the answer in the session
        request.session[f'q{q_order}'] = user_answer

        # Redirect to the next question
        return redirect('depistclic-get_question',
                        question_order=next_question_order)

    # Get the question for the GET request
    if question_order is None:
        question = Question.objects.first()
        context = {
            'question': question
            }
    else:
        # Redirects to synthesis view after last question
        if question_order > Question.objects.count():
            return redirect('depistclic-synthese')

        question = Question.objects.get(order=question_order)

        # A list for the displaying previous answers
        previous_answers = []
        for i in range(1, question_order):
            answer_key = f'q{i}'
            previous_answer = request.session.get(answer_key)
            if previous_answer is not None:
                previous_answers.append(previous_answer)

        context = {
            'question': question,
            'previous_answers': previous_answers,
        }

    return render(request, 'mainapp/questions.html', context)


# The synthesis page view
def synthese(request):
    # A list for the displaying previous answers
    previous_answers = []
    for i in range(1, Question.objects.count()):
        answer_key = f'q{i}'
        previous_answer = request.session.get(answer_key)
        if previous_answer is not None:
            previous_answers.append(previous_answer)

    context = {
        'previous_answers': previous_answers,
    }
    return render(request, 'mainapp/synthese.html', context)
