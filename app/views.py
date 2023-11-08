from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def madhu(request):
    return HttpResponse('<h1><marquee>and Sports along with News updates from around the world. Also, find English News, live</h1></marquee>')
