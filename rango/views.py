from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
 ##   return HttpResponse("Rango says hey there partner! <a href='/rango/about/'>About</a>")
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    return render(request, 'rango/index.html', context=context_dict)
def about(request):
    context_dict = {'boldmessage': 'This tutorial has been put together by Raphael Salguero'}
    return render(request, 'rango/about.html', context=context_dict)
