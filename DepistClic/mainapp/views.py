from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'mainapp/home.html')


def questions(request):
    return render(request, 'mainapp/questions.html')
