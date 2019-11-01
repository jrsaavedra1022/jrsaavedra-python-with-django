"""PLatzigram views """
from django.http import HttpResponse, JsonResponse

# utilities
from datetime import datetime
import json 

def hello_world(request):
	"""return a greeting"""
	now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
	return  HttpResponse("Oh hi! current server time is: {now}".format(
		now=str(now)
		))

def sorted_list(request):
	"""return a list oreder of numbers"""
	# para hacer debugger en python
	# import pdb; pdb.set_trace()
	numbers = request.GET['numbers']

	order_list = [int(number) for number in numbers.split(',')]
	order_list.sort()

	data = {
		'stutus': 'ok',
		'numbers': order_list,
		'message': 'Integer sort successfully!'
	}
	
	return HttpResponse(
		json.dumps(data, indent=4), 
		content_type="application/json"
		)
	# return JsonResponse(order_list, safe=False)


def say_hi(request, name, age):
	"""return a greeting"""
	if age < 12:
		message = 'Sorry {}, you are not allowed here'.format(name)
	else:
		message = 'Hello, {}! Welcome to Platzi!'.format(name)

	return HttpResponse(message)