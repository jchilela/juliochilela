from django.shortcuts import render
from django.http import  HttpResponse,HttpResponseRedirect


def en(request):
	template = 'en.html'
	return render(request,template)

def pt(request):
	template = 'pt.html'
	return render(request,template)


def mqtt(request):
	template = 'mqtt.html'
	return render(request,template)