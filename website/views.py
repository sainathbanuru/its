from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):

	template = 'website/index.html'

	points = data.objects.all()
	return render(request, template, {'points': points})


def news(request):
	return render(request, 'website/news.html', {})


def contact(request):
	return render(request, 'website/contact.html', {})




def redirect(request):

	latitude = request.POST['lat']
	longitude = request.POST['lng']
	page = request.POST['page']

	if page == "temp":
		return render(request, 'website/temperature.html', {})
	
	if page == "hum":
		return render(request, 'website/humidity.html', {})	

	if page == "co":
		return render(request, 'website/co2.html', {})

	if page == "smoke":
		return render(request, 'website/smoke.html', {})


def temperature(request):
	return render(request, 'website/temperature.html', {})

def humidity(request):
	return render(request, 'website/humidity.html', {})

def co2(request):
	return render(request, 'website/co2.html', {})

def smoke(request):
	return render(request, 'website/smoke.html', {})