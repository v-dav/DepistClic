from django.shortcuts import render, redirect
from .models import Question
from .forms import AnswerBinary, AnswerInteger, AnswerSex, CommentForm


# Calculates the BMI of the patient
def get_bmi(weight, height):
    height_meters = height / 100
    bmi = round(weight / (height_meters ** 2), 1)
    if bmi < 18.5:
        suffix = ": Maigreur"
    elif bmi >= 18.5 and bmi < 25:
        suffix = ": Corpulence normale"
    elif bmi >= 25 and bmi < 30:
        suffix = ": Surpoids"
    elif bmi >= 30 and bmi < 35:
        suffix = ": Obésité modérée"
    elif bmi >= 35 and bmi < 40:
        suffix = ": Obésité sévère"
    elif bmi >= 40:
        suffix = ": Obésité morbide"
    bmi_string = f'IMC {bmi}{suffix}'
    return bmi_string


# Calulates the renal desease stage
def irc_grade(dfg):
    if dfg >= 90:
        return "Stade I: pas d'atteinte de l'épuration rénale"
    elif dfg >= 60 and dfg < 90:
        return "Stade II: insuffisance rénale légère"
    elif dfg >= 45 and dfg < 60:
        return "Stade IIIA: insuffisance rénale modérée"
    elif dfg >= 30 and dfg < 45:
        return "Stade IIIB: insuffisance rénale modérée"
    elif dfg >= 15 and dfg < 30:
        return "Stade IV: insuffisance rénale sévère"
    elif dfg < 15:
        return "Stade V: insuffisance rénale terminale"


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

    # Start displaying "My Patient" values after second question
    if question.order > 1:
        # Questions where responses come with suffix after numeric value
        suffix = ['q2', 'q3', 'q4', 'q5', 'q6']

        # Get the values and calculate BMI if possible
        height = request.session.get('q3')
        weight = request.session.get('q4')
        if weight and height:
            bmi_string = get_bmi(weight, height)

        # Get the value and calculate renal desease stage if possible
        dfg = request.session.get('q6')
        if dfg:
            dfg_string = irc_grade(dfg)

        # A list for the displaying previous answers and score
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
                if i == 4 and bmi_string:
                    previous_answers.append(bmi_string)
                if i == 6 and dfg_string:
                    previous_answers.append(dfg_string)

        context['previous_answers'] = previous_answers

    return render(request, 'mainapp/questions.html', context)


# The synthesis page view
def synthese(request):
    # Questions where responses come with suffix after numeric value
    suffix = ['q2', 'q3', 'q4', 'q5', 'q6']

    # Get the values and calculate BMI if possible
    height = request.session.get('q3')
    weight = request.session.get('q4')
    if weight and height:
        bmi_string = get_bmi(weight, height)

    # Get the value and calculate renal desease stage if possible
    dfg = request.session.get('q6')
    if dfg:
        dfg_string = irc_grade(dfg)

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
            if i == 4 and bmi_string:
                previous_answers.append(bmi_string)
            if i == 6 and dfg_string:
                previous_answers.append(dfg_string)

    context = {
        'previous_answers': previous_answers,
    }
    return render(request, 'mainapp/synthese.html', context)


def comment_page(request):
    form_comment = CommentForm(request.POST or None)
    if form_comment.is_valid():
        form_comment.save()
        form_comment = CommentForm()

    context = {
        'form_comment': form_comment,
    }
    return render(request, 'mainapp/comment.html', context)
