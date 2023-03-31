from django.shortcuts import render
from django.views.generic.edit import CreateView
from .forms import QuestionForm
from .models import Question


# Create your views here.

def add_question(request):
    if request.method == 'POST':
        print(request.POST)
    context = {}
    return render(request, 'questions/add_question.html', context)


def get_question(request):
    questions = Question.objects.all()
    context = {'questions': questions}
    return render(request, 'questions/get_question.html', context)


def home(request):
    return render(request, 'questions/home.html')

# class QuestionCreateView(CreateView):
#     model = Question
#     form_class = QuestionForm
#     template_name = 'questions/add_question.html'
#     success_url = '/'
