from django.shortcuts import render

# Create your views here.
def a1_first(request):
    d={'a':80,'b':50,'c':20}
    return render(request,'a1_first.html',d)

def a1_second(request):
    d={'a':100,'b':50,'c':25}
    return render(request,'a1_second.html',d)

