from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateView
from administration.models import *
from website.models import *
from datetime import date
import time
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect,HttpResponse

html_for_student = "<br><br><center><h1>You are not authorized to use this page</h1><br><a href="
html_for_student += "http://127.0.0.1:8000"
html_for_student += ">Go to User page</a></center>"



class home(TemplateView):
    
    def get(request, self, *args, **kwargs):

    	d = data.objects.all()
    	D = []

    	for i in d:
    		
    		l = [i.h_id, i.latitude, i.longitude, i.source]
    		if l not in D:
    			D.append(l)


    	return render(request, 'administration/home.html', {'data': D, 'full_data': d})
    #if request.user.groups.filter(name='admin').exists():