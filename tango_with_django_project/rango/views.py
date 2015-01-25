from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says here is the about page. <br/> <a href='/rango/about'>About</a>")

def about(request):
	return HttpResponse("<a href='/rango/'>Index</a> This tutorial has been put together by Alex Leet, 2090140L")