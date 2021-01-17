from django.shortcuts import render
from django.http import HttpResponse
import random


# Create your views here.


#def home(request):
#	return HttpResponse('<h1>This is HOME</h1>')

def home(request):
	return render(request, 'generator/home.html', {'password':'aaffdahfgd'})

def password(request):
	passw = ''
	char = list('abcdefghijklmnopqrstuvwxyz')

	if request.GET.get('uppercase'):
		char.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
	if request.GET.get('special'):
		char.extend(list('!@#$%^&*()-+'))
	if request.GET.get('numbers'):
		char.extend(list('1234567890'))

	length = int(request.GET.get('length', 12))
	for x in range(length):
		passw += random.choice(char)
	
	return render(request, 'generator/password.html', {'password':passw})

def about(request):
	return render(request, 'generator/about.html')


