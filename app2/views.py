from django.shortcuts import render

# Create your views here.
def a2_first(request):
    d={'a':1000,'b':500,'c':250}
    return render(request,'a2_first.html',d)

def a2_second(request):
    d={'name':'chaithu'}
    return render(request,'a2_second.html',d)