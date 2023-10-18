from django.shortcuts import render, redirect
from .models import Question
from .forms import AnswerBinary, AnswerInteger, AnswerSex


# Homepage view
def home(request):
    request.session.clear()
    return render(request, 'mainapp/home.html')


# The view that stores the answer in a session and gets a question
def get_question(request, question_order=None):
    # Get the first question
    if question_order is None:
        question = Question.objects.first()
    else:
        # Redirects to synthesis view after last question
        if question_order > Question.objects.count():
            return redirect('depistclic-synthese')

        # Get the question if not the first question
        question = Question.objects.get(order=question_order)

    # Create a bool form
    if question.order == 1:
        form_bool = AnswerSex(request.POST or None,
                              initial={'question_order': question.order})
    else:
        form_bool = AnswerBinary(request.POST or None,
                                 initial={'question_order': question.order})
    if form_bool.is_valid():
        user_answer = form_bool.cleaned_data['response']
        print(user_answer)

        # Convert the bool answer
        if not isinstance(form_bool, AnswerSex):
            if user_answer == 'True':
                user_answer = True
            else:
                user_answer = False

        q_order = form_bool.cleaned_data['question_order']
        # Store the answer in the session
        request.session[f'q{q_order}'] = user_answer
        print(request.session[f'q{q_order}'])
        next_question_order = q_order + 1
        # Redirect to the next question
        return redirect('depistclic-get_question',
                        question_order=next_question_order)

    # Create int form
    form_int = AnswerInteger(request.POST or None,
                             initial={'question_order': question.order})
    if form_int.is_valid():
        user_answer = int(form_int.cleaned_data['response'])
        q_order = form_int.cleaned_data['question_order']
        # Store the answer in the session
        request.session[f'q{q_order}'] = user_answer
        next_question_order = q_order + 1
        # Redirect to the next question
        return redirect('depistclic-get_question',
                        question_order=next_question_order)

    context = {
            'question': question,
            'form_bool': form_bool,
            'form_int': form_int
        }

    if question.order > 1:
        suffix = ['q2', 'q3', 'q4', 'q5', 'q6']
        # A list for the displaying previous answers
        previous_answers = []
        for i in range(1, question_order + 1):
            previous_question = Question.objects.get(order=i)
            answer_key = f'q{i}'
            previous_answer = request.session.get(answer_key)
            # If not none and not false
            if previous_answer:
                if answer_key in suffix:
                    previous_answer_fulltext = f'{previous_answer} {previous_question.display_text}'
                elif answer_key == 'q1':
                    previous_answer_fulltext = previous_answer
                else:
                    previous_answer_fulltext = previous_question.display_text
                previous_answers.append(previous_answer_fulltext)

        context['previous_answers'] = previous_answers

    return render(request, 'mainapp/questions.html', context)


# The synthesis page view
def synthese(request):
    suffix = ['q2', 'q3', 'q4', 'q5', 'q6']
    # A list for the displaying previous answers
    previous_answers = []
    for i in range(1, Question.objects.count() + 1):
        previous_question = Question.objects.get(order=i)
        answer_key = f'q{i}'
        previous_answer = request.session.get(answer_key)
        if previous_answer:
            if answer_key in suffix:
                previous_answer_fulltext = f'{previous_answer} {previous_question.display_text}'
            elif answer_key == 'q1':
                previous_answer_fulltext = previous_answer
            else:
                previous_answer_fulltext = previous_question.display_text
            previous_answers.append(previous_answer_fulltext)

    context = {
        'previous_answers': previous_answers,
    }
    return render(request, 'mainapp/synthese.html', context)
