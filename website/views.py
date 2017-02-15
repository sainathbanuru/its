from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.edit import FormView
from .models import *
from .forms import *
from django.views.generic.base import TemplateView
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):

	template = 'website/index.html'
	points = data.objects.all()
	return render(request, template, {'points': points})


def news(request):
	return render(request, 'website/news.html', {})


def contact(request):
	return render(request, 'website/contact.html', {})




def redirect(request, lat, lng, page):

	
	Data = data.objects.filter(latitude=lat).filter(longitude=lng)
	
	if page == "temp":
		return render(request, 'website/temperature.html', {'data': Data, 'lat': lat, 'lng': lng})
	
	if page == "hum":
		return render(request, 'website/humidity.html', {'data': Data, 'lat': lat, 'lng': lng})	

	if page == "co":
		return render(request, 'website/co2.html', {'data': Data, 'lat': lat, 'lng': lng})

	if page == "smoke":
		return render(request, 'website/smoke.html', {'data': Data, 'lat': lat, 'lng': lng})


def temperature(request):
	return render(request, 'website/temperature.html', {})

def humidity(request):
	return render(request, 'website/humidity.html', {})

def co2(request):
	return render(request, 'website/co2.html', {})

def smoke(request):
	return render(request, 'website/smoke.html', {})


@method_decorator(login_required, name='dispatch')
class insert(FormView):

	template_name = 'website/insert.html'
	form_class = insert_form
	

	def get(self, request, *args, **kwargs):
		form = self.form_class(None)
		context = {
			'form' : form
		}

		return render(request, self.template_name, context)


	def post(self, request, **kwargs):

		form = insert_form(request.POST)
		context = {'form' : self.form_class(None)}

		if form.is_valid():

			if request.POST['latitude'] < 0:
				context["error_message"] = "Invalid latitude"
			if request.POST['longitude'] < 0:
				context["error_message"] = "Invalid longitude"
			if request.POST['temperature'] < 0:
				context["error_message"] = "Invalid temperature"
			if request.POST['humidity'] < 0:
				context["error_message"] = "Invalid humidity"
			if request.POST['co2'] < 0:
				context["error_message"] = "Invalid Co2"
			if request.POST['smoke'] < 0:
				context["error_message"] = "Invalid smoke"

			D = data()
			D.latitude = float(request.POST['latitude'])
			D.longitude = float(request.POST['longitude'])
			D.temperature = request.POST['temperature']
			D.humidity = request.POST['humidity']
			D.co2 = request.POST['co2']
			D.smoke = request.POST['smoke']
			D.save()

			context["message"] = "Data Inserted !!"

			return render(request, self.template_name, context)

		return render(request, self.template_name, {'form' : self.form_class(None)})

class login_user(TemplateView):
	template_name = 'website/login.html'
	def get(self, request, *args, **kwargs):
		return render(request,self.template_name,{})

	def post(self, request,*args, **kwargs):
		username = request.POST['email']
		password = request.POST['pass']
		#return HttpResponse(username+password)
		user = authenticate(username=username, password=password)
		#return HttpResponse(user)
		print(user)
		if user is not None:
			if user.is_active:
				login(request, user)
				#return HttpResponse("login")
				return render(request, 'website/index.html', {})
			else:
				return render(request, 'website/login.html', {'error_message': 'Your account has been disabled'})
		else:
			return render(request, 'website/login.html', {'error_message': 'Invalid login'})

def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')
