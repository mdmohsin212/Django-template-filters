from django.shortcuts import render
import datetime

def home(request):
    data = {'info' : ['my', 'name', 'is', 'siam'], 'timeNow' : datetime.datetime.now(), 'name' : 'siam', 'city' : 'D H A K A', 'peoples' : [
    {'name': 'Josh', 'age': 37},
    {'name': 'Dave', 'age': 19},
    {'name': 'Joe', 'age': 31},
    ], 'pet' : 'i HaVe cAT', 'py' : 'I love python. it is easy',}
    return render(request, 'home.html', data)