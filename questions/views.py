from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Question


# Create your views here.

def add_question(request):
    if request.method == 'POST':
        checked_input_values = request.POST.getlist('right_answers')
        input_values = request.POST.getlist('answers')
        answers = []
        right_answers = []
        for answer in input_values:
            answers.extend(answer.split(','))
        for right_answer in checked_input_values:
            right_answers.extend(right_answer.split(','))
        question = request.POST.get('question')
        if question is None:
            question = request.FILES['file']
        description = request.POST.get('description')
        commitQs(answers, right_answers, question, description)

    context = {}
    return render(request, 'questions/add_question.html', context)


def commitQs(answers, right_answers, question, description):
    if isinstance(question, str):
        question = Question(name=question, description=description)
        question.save()
        for answer in answers:
            question.answers_set.create(answer=answer, is_correct=answer in right_answers)
    else:
        question = Question(attachment=question, description=description)
        question.save()
        for answer in answers:
            question.answers_set.create(answer=answer, is_correct=answer in right_answers)
    return {"status": "success"}


def get_question(request):
    return render(request, 'questions/get_question.html')


def get_object(request, id):
    question = get_object_or_404(Question, id=id)
    if question.attachment:
        file_url = question.attachment.url
        data = {'file_url': file_url}
    else:
        data = {'question': question.name}
    return JsonResponse(data)
