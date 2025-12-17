from django.shortcuts import render
from django.http import HttpResponse




# Create your views here.
def hello_world(request):
    user = request.user

    return render(request, template_name="hello.html", context={
        "user": user
    })
    
def hello_world2(request):
    user = request.user

    return render(request, template_name="hello2.html", context={
        "user": user
    })