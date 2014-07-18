from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from polls.models import *

# Create your views here.
def index(request):
	# lastest_poll_orderby_date = Poll.objects.order_by('-pub_date')[:5]
	lastest_poll_orderby_date = Poll.objects.order_by('-pub_date')
	# output = ','.join([p.question for p in lastest_poll_orderby_date])
	template = loader.get_template('polls/index.html')
	context = RequestContext(request,
			{'lastest_poll_orderby_date': lastest_poll_orderby_date},
		)
	return HttpResponse(template.render(context))

def detail(request, poll_id):
	return HttpResponse('You are looking at Poll %s.' % poll_id)

def result(request, poll_id):
	return HttpResponse('You are looking the result of Poll %s.' % poll_id)

def vote(request, poll_id):
	return HttpResponse('You are voting the Poll %s' % poll_id)