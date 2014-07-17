from django.contrib import admin
from models import Poll,Choice

# Register your models here.
# class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 3

class PollAdmin(admin.ModelAdmin):
	# fields = ['pub_date','question']
	fieldsets = [
		('Time Infomation',{'fields':['pub_date']}),
		('Data Infomation',{'fields':['question'],'classes':['collapse']}),
	]
	inlines = [ChoiceInline]
	list_display = ['question','pub_date','was_published_recently']
	list_filter = ['pub_date','question']
	search_fields = ['question']

admin.site.register(Poll,PollAdmin)
# admin.site.register(Choice)
