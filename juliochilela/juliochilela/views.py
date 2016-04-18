from django.shortcuts import render
from django.http import  HttpResponse,HttpResponseRedirect


def index(request):
	template = 'index.html'
	return render(request,template)