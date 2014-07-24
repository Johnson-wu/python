#coding:utf-8

import datetime

from django.test import TestCase
from django.utils import timezone
from django.core.urlresolvers import reverse

from models import Poll

# Create your tests here.
def create_poll(question, days):
	return Poll.objects.create(question=question, pub_date=timezone.now() + datetime.timedelta(days=days))

class PollMethodTests(TestCase):
	def test_was_published_recently_future_poll(self):
		future_poll = Poll(pub_date=timezone.now() + datetime.timedelta(days=20))
		self.assertEqual(future_poll.was_published_recently(),False)

	def test_was_published_recently_old_poll(self):
		old_poll = Poll(pub_date=timezone.now() -  datetime.timedelta(days=2))
		self.assertEqual(old_poll.was_published_recently(),False)

	def test_was_published_recently_recent_poll(self):
		recent_poll = Poll(pub_date=timezone.now() - datetime.timedelta(hours=10))
		self.assertEqual(recent_poll.was_published_recently(),True)


class PollViewTests(TestCase):
	def test_index_view_with_no_poll(self):
		response = self.client.get(reverse('polls:index'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'No polls are available')
		self.assertQuerysetEqual(response.context['lastest_poll_orderby_date'], [])

	def test_index_view_with_past_poll(self):
		create_poll('A past poll', -30)
		response = self.client.get(reverse('polls:index'))
		self.assertQuerysetEqual(response.context['lastest_poll_orderby_date'], ['<Poll:A past poll>'])

