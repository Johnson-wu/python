from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
# from django.template import RequestContext, loader
from django.core.urlresolvers import reverse

from polls.models import *

# Create your views here.
def index(request):
	lastest_poll_orderby_date = Poll.objects.order_by('-pub_date')

	context = {'lastest_poll_orderby_date': lastest_poll_orderby_date}
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
    poll = get_object_or_404(Poll, pk=poll_id)
	# return HttpResponse('You are looking the result of Poll %s.' % poll_id)
    return render(request, 'polls/result.html', {'poll':poll})

def vote(request, poll_id):
	poll = get_object_or_404(Poll, pk=poll_id)
	try:
		# assert not poll,poll
		# assert request.POST['choice']==10, request.POST['choice']
        # x = request.POST['choice']
		select_choice = poll.choice_set.get(pk=request.GET['choice'])
	except (KeyError, Choice.DoesNotExist):
		return render(request,'polls/detail.html',{
				'poll': poll,
				'error_message': 'You did not select a choice.'
			})
	else:
		select_choice.votes += 1
		select_choice.save()
		return HttpResponseRedirect(reverse('polls:result',args=(poll.id,)))
        # return HttpResponse(reverse('polls:result',args=(poll.id,)))
