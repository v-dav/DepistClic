from django.shortcuts import render, redirect
from .models import Question, ScreeningTest
from .forms import AnswerBinary, AnswerInteger, AnswerSex, CommentForm
from django.core.validators import MinValueValidator, MaxValueValidator


# Calculates the BMI of the patient
def get_bmi_string(weight, height):
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
    if question.order == 1:  # What is patient's sex ?
        form_bool = AnswerSex(request.POST or None,
                              initial={'question_order': question.order})
    else:
        form_bool = AnswerBinary(request.POST or None,
                                 initial={'question_order': question.order})
    if form_bool.is_valid():
        user_answer = form_bool.cleaned_data['response']

        # Convert the bool answer
        if not isinstance(form_bool, AnswerSex):
            if user_answer == 'True':
                user_answer = True
            else:
                user_answer = False

        # The suite of the logic with bool form
        q_order = form_bool.cleaned_data['question_order']
        # Store the answer in the session
        request.session[f'q{q_order}'] = user_answer
        next_question_order = q_order + 1
        # Redirect to the next question
        return redirect('depistclic-get_question',
                        question_order=next_question_order)

    # Create int form
    form_int = AnswerInteger(request.POST or None,
                             initial={'question_order': question.order})

    # Customize validation of int form depending on the question
    if question.order == 2:  # Age
        form_int.fields['response'].validators = [MinValueValidator(
            15,
            message='Âge minimum: 15 ans')]
        form_int.fields['response'].validators.append(MaxValueValidator(
            105,
            message='Âge maximum: 105 ans'))
    elif question_order == 3:  # Height
        form_int.fields['response'].validators = [MinValueValidator(
            130,
            message='Taille minimum: 130 cm')]
        form_int.fields['response'].validators.append(MaxValueValidator(
            220,
            message='Taille maximum: 220 cm'))
    elif question_order == 4:  # Weight
        form_int.fields['response'].validators = [MinValueValidator(
            30,
            message='Poids minimum: 30 kg')]
        form_int.fields['response'].validators.append(MaxValueValidator(
            200,
            message='Poids maximum: 200 kg'))
    elif question_order == 5:  # Diabetes evolution
        form_int.fields['response'].validators.append(MaxValueValidator(
            70,
            message='Valeur maximale autorisée: 70'))
    elif question_order == 6:  # DFG Rate
        form_int.fields['response'].validators.append(MaxValueValidator(
            150,
            message='Valeur maximale autorisée: 150'))

    # The suite of the logic with int form
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
        bmi_string = None
        if weight and height:
            bmi_string = get_bmi_string(weight, height)

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
                    previous_answer_fulltext = \
                        f'{previous_answer} {previous_question.display_text}'
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
    bmi_string = None
    bmi = None
    if weight and height:
        bmi_string = get_bmi_string(weight, height)
        height_meters = height / 100
        bmi = round(weight / (height_meters ** 2), 1)

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
                previous_answer_fulltext = \
                    f'{previous_answer} {previous_question.display_text}'
            elif answer_key == 'q1':
                previous_answer_fulltext = previous_answer
            else:
                previous_answer_fulltext = previous_question.display_text
            previous_answers.append(previous_answer_fulltext)
            if i == 4 and bmi_string:
                previous_answers.append(bmi_string)
            if i == 6 and dfg_string:
                previous_answers.append(dfg_string)

    # Get systematic annual screening tests from the database
    systematic_annual_tests = \
        ScreeningTest.objects.filter(frequency='Annuel',
                                     type='Systématique').order_by('title')
    annual_tests = systematic_annual_tests

    # Get systematic important reminder from the database
    systematic_reminders = ScreeningTest.objects.filter(
        frequency='Rappels importants',
        type='Systématique').order_by('title')
    reminders = systematic_reminders

    # Create initial context
    context = {
        'previous_answers': previous_answers,
        'annual_tests': annual_tests,
        'reminders': reminders
    }

    # Get and add conditional screening tests to the context

    # NT-proBNP
    if (bmi and bmi >= 30) or \
            (request.session.get('q1') == 'Femme') or \
            (request.session.get('q7')) or \
            (request.session.get('q8')) or \
            (request.session.get('q9')) or \
            (request.session.get('q10')) or \
            (request.session.get('q29')) or \
            (dfg and dfg < 90):
        context['annual_tests'] = context['annual_tests'] | \
            ScreeningTest.objects.filter(title__icontains='NT-proBNP')

    # Erectile dysfonction
    if request.session.get('q1') == 'Homme':
        context['annual_tests'] = context['annual_tests'] | \
            ScreeningTest.objects.filter(title__icontains='érectile')

    # B12 testing
    metformin = request.session.get('q12')
    if metformin:
        context['annual_tests'] = context['annual_tests'] | \
            ScreeningTest.objects.filter(title__icontains='B12')

    conditional_specialist_tests = []

    # AOMI
    aomi = request.session.get('q11')
    if aomi:
        conditional_specialist_tests.append(ScreeningTest.objects.get(
            title__icontains='AOMI'))

    # AAA screening
    sex = request.session.get('q1')
    age = request.session.get('q2')
    tobacco = request.session.get('q13')
    atcd_aaa = request.session.get('q28')

    if (sex == 'Homme' and age and age >= 65 and age <= 75 and tobacco) or \
            (age and age >= 50 and age <= 75 and atcd_aaa):
        conditional_specialist_tests.append(ScreeningTest.objects.get(
            title__icontains='AAA'))

    # Pancreas cancer
    diabetes_duration = request.session.get('q5')
    chronic_pancreatitis = request.session.get('q26')
    difficult_diabetes = request.session.get('q9')
    weight_loss = request.session.get('q27')

    if (chronic_pancreatitis and diabetes_duration
        and diabetes_duration < 2) or \
            (chronic_pancreatitis and difficult_diabetes) or \
            (diabetes_duration and diabetes_duration < 2 and age and age >= 50
             and bmi and bmi >= 18.5 and bmi <= 25) or \
            (diabetes_duration and diabetes_duration < 2 and weight_loss):
        conditional_specialist_tests.append(ScreeningTest.objects.get(
                         title__icontains='TDM-TAP'))

    # Bariatric surgery
    saos = request.session.get('q24')
    nash = request.session.get('q25')
    hta = request.session.get('q8')

    if (age and age < 60) and bmi and \
        ((bmi >= 40) or (bmi >= 35 and hta) or (bmi >= 35 and saos) or
         (bmi >= 35 and nash)):
        conditional_specialist_tests.append(ScreeningTest.objects.get(
                         title__icontains='bariatrique'))

    # Liver desease
    dylipidemy = request.session.get('q7')
    if bmi and bmi >= 25 and hta and dylipidemy:
        conditional_specialist_tests.append(ScreeningTest.objects.get(
                         title__icontains='stéatopathie'))

    # Cushing syndrome
    if bmi and bmi >= 25 and hta and dylipidemy and difficult_diabetes:
        conditional_specialist_tests.append(ScreeningTest.objects.get(
                         title__icontains='Cushing'))
    
    # Exercice effort test
    if request.session.get('q23') or \
            aomi or \
            hta or \
            request.session.get('q18') or \
            request.session.get('q17') or \
            request.session.get('q16') or \
            (dfg and dfg < 90) or \
            request.session.get('q20') or \
            request.session.get('q10') or \
            request.session.get('q22') or \
            request.session.get('q21') or \
            (diabetes_duration and diabetes_duration > 10) or \
            request.session.get('q19') or \
            request.session.get('q15') or \
            request.session.get('q14') or \
            tobacco or dylipidemy:
        conditional_specialist_tests.append(ScreeningTest.objects.get(
                        title__icontains='effort'))

    # Vein preservation and hepatitis B
    if dfg and dfg < 45:
        context['reminders'] = context['reminders'] | \
            ScreeningTest.objects.filter(title__icontains='veineux')
        context['reminders'] = context['reminders'] | \
            ScreeningTest.objects.filter(title__icontains='anti-hépatite B')

    # Zona
    if age and age > 65 and age < 74:
        context['reminders'] = context['reminders'] | \
            ScreeningTest.objects.filter(title__icontains='zona')

    if conditional_specialist_tests:
        context['conditional_specialist_tests'] = conditional_specialist_tests

    return render(request, 'mainapp/synthese.html', context)


def contact(request):
    return render(request, 'mainapp/contact.html')


def comment_page(request):
    form_comment = CommentForm(request.POST or None)
    if form_comment.is_valid():
        form_comment.save()
        form_comment = CommentForm()

    context = {
        'form_comment': form_comment,
    }
    return render(request, 'mainapp/comment.html', context)


def team(request):
    return render(request, 'mainapp/team.html')


def mission(request):
    return render(request, 'mainapp/mission.html')
