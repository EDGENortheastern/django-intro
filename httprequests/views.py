from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'httprequests/home.html')

def hello(request):
    the_name = request.GET.get('name')
    return render(request, 'httprequests/hello.html', {'name':the_name})
