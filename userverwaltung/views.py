from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    contens = {
        'name': request.user
    }
    return render(request, 'hello.html', contens)