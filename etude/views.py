from django.shortcuts import render
from django.http import HttpResponse

def home_view(request, *args, **kwargs):
    #return HttpResponse("<h1> hello world </h1>")
    return render(request, "home.html", {})
def contact_view(request, *args, **kwargs):
    return HttpResponse("<h1> hello contact</h1>")
def about_ebios_view(request, *args, **kwargs):
    return HttpResponse("<h1> hello ebios </h1>")