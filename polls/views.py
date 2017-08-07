# -*- coding: utf-8 -*-
from __future__ import unicode_literals

#from django.shortcuts import render
from django.template import loader
# Create your views here.
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Question,Choice


def index(request):
    latest_question_list=Question.objects.order_by('-pub_date')[:5]
    template=loader.get_template('polls/index.html')
    context={'latest_question_list':latest_question_list}
    return HttpResponse(template.render(context,request))

def detail(request,question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/detail.html', {'question': question})   
def results(request,choice_id):
	result = get_object_or_404(Choice, pk=choice_id)
	return render(request, 'polls/results.html', {'result': result})
def vote(request,choice_id):
	vo = get_object_or_404(Choice, pk=choice_id)
	return render(request, 'polls/vote.html', {'vo': vo})

