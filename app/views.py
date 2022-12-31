from django.shortcuts import render

# Create your views here.
def asif(request):
    d={'a':10,'b':15}
    return render (request,'asif.html',d)