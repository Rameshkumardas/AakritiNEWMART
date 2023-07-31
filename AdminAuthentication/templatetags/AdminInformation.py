from django import template
from AdminAuthentication.models import AdminRegistration

register = template.Library()

@register.simple_tag
def HiAdmin():
	import datetime, pytz
	from django.conf import settings
	cur_time = datetime.datetime.now(tz=pytz.timezone(str(settings.TIME_ZONE)))
	if cur_time.hour < 12:
		return 'Good Morning'
	elif 12 <= cur_time.hour < 18:
		return 'Good Afternoon'
	else:
		return 'Good Evening'

