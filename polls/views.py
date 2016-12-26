from django.shortcuts import render
from django.http import HttpResponse
from .models import Question


def index(request):
    latest_questoin_list = Question.objects.order_by('pub_date')[:5:-1]
    output = ', '.join([q.question_text for q in latest_questoin_list])
    return HttpResponse(output)

def detail(request, question_id):
    response = "You're looking at question {}".format(question_id)
    return HttpResponse(response)


def results(request, question_id):
    result = "You're looking at the results of question {}".format(question_id)
    return HttpResponse(result)


def vote(request, question_id):
    return HttpResponse("Yo're voting on question {}".format(question_id))

