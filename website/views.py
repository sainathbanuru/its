#from django.contrib.gis.geoIP import GeoIP
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
import datetime
from django.contrib.auth import authenticate,login, logout

# Create your views here.
def index(request):

	#g = GeoIP()
	#lat,lng = g.lat_lon(user_ip)
	#print "\n\n\n\n", lat, lng, "\n\n\n\n\n\n"
	template = 'website/index.html'
	points = set(data.objects.all())
	return render(request, template, {'points': points})


def news(request):
	return render(request, 'website/news.html', {})


def contact(request):
	return render(request, 'website/contact.html', {})



def redirect(request, lat, lng):
	
	Data = data.objects.filter(latitude=lat).filter(longitude=lng)
	current_date = datetime.datetime.now()
	
	this_day_data = []
	this_week_data = []

	for i in Data:

		if (i.year == current_date.year) and (i.month == current_date.month):
			
			if i.day == current_date.day:
				this_day_data.append(i)
			

			if current_date.day >= 7:
				if i.day >= current_date.day - 7:
					this_week_data.append(i)
			else:
				this_week_data.append(i)


	dic = {}
	for i in this_week_data:

		if i.day in dic:
			dic[i.day].append(i)
		else:
			dic[i.day] = [i]

	this_week_data = []
	for i in dic:

		temp = data()
		temp.latitude = dic[i][0].latitude
		temp.longitude = dic[i][0].longitude
		temp.day = dic[i][0].day

		temp.temperature = sum([j.temperature for j in dic[i]])*1.0	/len(dic[i])
		temp.humidity = sum([j.humidity for j in dic[i]])*1.0/len(dic[i])
		temp.co2 = sum([j.co2 for j in dic[i]])*1.0/len(dic[i])
		temp.smoke = sum([j.smoke for j in dic[i]])*1.0/len(dic[i])

		this_week_data.append(temp)



	dic = {}
	for i in this_day_data:

		if i.hour in dic:
			dic[i.hour].append(i)
		else:
			dic[i.hour] = [i]

	this_day_data = []
	for i in dic:

		temp = data()
		temp.latitude = dic[i][0].latitude
		temp.longitude = dic[i][0].longitude
		temp.hour = dic[i][0].hour

		temp.temperature = sum([j.temperature for j in dic[i]])*1.0/len(dic[i])
		temp.humidity = sum([j.humidity for j in dic[i]])*1.0/len(dic[i])
		temp.co2 = sum([j.co2 for j in dic[i]])*1.0/len(dic[i])
		temp.smoke = sum([j.smoke for j in dic[i]])*1.0/len(dic[i])

		this_day_data.append(temp)


	return render(request, 'website/show_data.html', {'data': this_day_data, 'week_data': this_week_data, 'lat': lat, 'lng': lng})
	

def show_data(request):
	return render(request, 'website/show_data.html', {})

def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')




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



def current_data(request, lat, lng, temp, humid, carbon, smo, source, h_id):


	current_date = datetime.date.today()

	current = data(
			latitude = lat,
			longitude = lng,
			temperature = temp,
			humidity = humid,
			co2 = carbon,
			smoke = smo,
			source = source,
			h_id = h_id,

			year = current_date.year,
			month = current_date.month,
			day = current_date.day,
			hour = current_date.hour
	)
	current.save()
	return HttpResponse("insertd")



class login(TemplateView):


    template_name = 'website/login.html'

    def get(self, request, *args, **kwargs):
        return render(request,self.template_name,{})


    def post(self, request, *args, **kwargs):
        if "?next" in request.POST:
            return HttpResponse(request.POST['next'])
        username = request.POST['email']
        password = request.POST['pass']
        #return HttpResponse(username+password)
        user = authenticate(username=username, password=password)
       # return HttpResponse(user)
        print(user)
        if user is not None:
            if user.is_active:
                if "next" in request.POST:
                	return HttpResponse(request.POST['next'])
                #return HttpResponse("Logged iN")
                 
                d = data.objects.all()
                D = []

                for i in d:
					
                    l = [i.h_id, i.latitude, i.longitude, i.source]
                    if l not in D:
                        D.append(l)

                    return render(request, 'website/administrator.html', {'data': D, 'full_data': d})

            else:
                return render(request, 'website/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'website/login.html', {'error_message': 'Invalid login'})


@login_required
def administrator(request):
    
	d = data.objects.all()
	D = []

	for i in d:
		
		l = [i.h_id, i.latitude, i.longitude, i.source]
		if l not in D:
			D.append(l)


	return render(request, 'website/administrator.html', {'data': D, 'full_data': d})