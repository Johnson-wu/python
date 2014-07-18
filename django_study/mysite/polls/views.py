from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
# from django.template import RequestContext, loader

from polls.models import *

# Create your views here.
def index(request):
	# lastest_poll_orderby_date = Poll.objects.order_by('-pub_date')[:5]
	lastest_poll_orderby_date = Poll.objects.order_by('-pub_date')
	# output = ','.join([p.question for p in lastest_poll_orderby_date])
	# template = loader.get_template('polls/index.html')
	# context = RequestContext(request,
	# 		{'lastest_poll_orderby_date': lastest_poll_orderby_date},
	# 	)
	context = {'lastest_poll_orderby_date': lastest_poll_orderby_date}
	# return HttpResponse(template.render(context))
	return render(request, 'polls/index.html', context)

def detail(request, poll_id):	
	# try:
	# 	poll = Poll.objects.get(pk=poll_id)
	# except Poll.DoesNotExist, e:
	# 	raise Http404

	# a shortcut : get_object_or_404
	poll = get_object_or_404(Poll, pk=poll_id)
	return render(request, 'polls/detail.html', {'poll': poll})

def result(request, poll_id):
	return HttpResponse('You are looking the result of Poll %s.' % poll_id)

def vote(request, poll_id):
	return HttpResponse('You are voting the Poll %s' % poll_id)