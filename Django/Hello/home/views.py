from multiprocessing import context
from django.shortcuts import render, HttpResponse
# render use for run templaets

# Create your views here.
def index(request):
    context = {
        "variable": "this is using variable",
        "variable1": "this code wrote in views.py file"

    }
    return render(request, 'index.html', context)
   # return render(request, 'index.html')
   # return HttpResponse("This is Home Page")
def about(request):
    return HttpResponse("This is About Page")
def services(request):
    return HttpResponse("This is Services Page")
def contact(request):
    return HttpResponse("This is Contact Page")