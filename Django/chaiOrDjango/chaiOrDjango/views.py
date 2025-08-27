from django.http import HttpResponse

from django.shortcuts import render


def home(request):
    # return HttpResponse("HRllo you are at home")
    return render(request,'index.html')

def about(request):
    return HttpResponse("Helllo u are at about")
