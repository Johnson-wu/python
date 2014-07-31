import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Poll(models.Model):
	question = models.CharField(max_length=200)
	pub_date = models.DateTimeField('Date published')

	# On python3 , that should be __str__(self)
	def __unicode__(self):
		return self.question

	def was_published_recently(self):
		return timezone.now() - datetime.timedelta(days=1) <= self.pub_date <= timezone.now()

	was_published_recently.admin_order_field = 'pub_date'	# sorted by pub_date
	was_published_recently.boolean = True
	was_published_recently.shortcut_description = 'Published recently ?'


class Choice(models.Model):
	poll = models.ForeignKey(Poll)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)

	def __unicode__(self):
		return self.choice_text


