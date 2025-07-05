from django.shortcuts import render,redirect
from django.http import HttpResponse
def home(request):
    result = None
    if request.method =='POST':
        a=int(request.POST.get('num1'))
        b=int(request.POST.get('num2'))
        O=request.POST.get('op')
        if O == 'add':
            result=a+b
        #return render(request,'home.html',{'result':result})
        return redirect('hello',result)
    return render(request,'home.html')
def hello(request,result):
    return render(request,'result.html',{'result':result})
# Create your views here.
 