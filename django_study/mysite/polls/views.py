from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from polls.models import Poll,Choice

# Create your views here.
class IndexView(generic.ListView):
    # model = Poll
    template_name = 'polls/index.html'
    context_object_name = 'lastest_poll_orderby_date'

    def get_queryset(self):
        return Poll.objects.order_by('-pub_date')


class DetailView(generic.DetailView):
    model = Poll
    template_name = 'polls/detail.html'


class ResultView(generic.DetailView):
    model = Poll
    template_name = 'polls/result.html'



def vote(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    try:
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
