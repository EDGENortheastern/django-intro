from django.shortcuts import render

# Create your views here.

def do_things():
    return "Do"

def home(request):
    return render(request, 'httprequests/home.html')

def hello(request):
    the_name = request.GET.get('name')
    return render(request, 'httprequests/hello.html', {'name':the_name})
