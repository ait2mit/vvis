from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
import numpy as np

from django.views.generic import ListView,CreateView, UpdateView, DeleteView
import pickle
import json
from .models import retail
# from .forms import *
from django.contrib.auth.decorators import login_required
# from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.csrf import csrf_exempt
# from .models import PicPost

# Create your views here.
import random
random.seed(10)
get_colors = lambda n: list(map(lambda i: "#" + "%06x" % random.randint(0, 0xFFFFFF),range(n)))


def home(request):
	st=retail.objects.all()
	# return HttpResponse(st)
	return render(request=request, template_name="index.html", context={"st":st})





def biontech_chart1(request):
	st = {"labels": ['Hispanic or Latino', 'Not Hispanic or Latino',"American Indian or Alaska native","Asian", "Black or African American", "Native Hawaiian or other Pacific Islander","White"],
	"data": [94.5, 94.7,100, 74.4,100,100,95.4],
	"colors": get_colors(7)

	      }
	return render(request=request, template_name="index.html", context={"st":st})














class DataCreateView(CreateView):
	model = retail
	fields = ['enrl_no','first_name','last_name','age','batch','course','address']
	template_name="data_insert.html"

	def form_valid(self, form):
		return super().form_valid(form)

class DataUpdateView(UpdateView):
	model = retail
	fields = ['enrl_no','first_name','last_name','age','batch','course','address']
	template_name="data_update.html"
	def form_valid(self, form):
		return super().form_valid(form)


class DataDeleteView(DeleteView):
	model=retail
	success_url="/"
	template_name = "retail_confirm_delete.html"


def about(request):
	return render(request=request,template_name="about.html", context={})
