from django.shortcuts import render

# Create your views here.

def square_num(num):
    return num**2

class Avatar:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name + 'lalala'

def home(request):
    return render(request, 'httprequests/home.html')

def hello(request):
    the_name = request.GET.get('name')
    the_number = request.GET.get('number')
    ava = Avatar(the_name)
    return render(request, 'httprequests/hello.html', {'name':the_name, 'number':the_number})
