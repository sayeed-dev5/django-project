from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Contract



def dashboard(request):
    return render(request, 'home.html')

def home(request):
    return render(request, 'home.html')

def blog(request):
    return render(request, 'blog.html')

def about(request):
    return render(request, 'about.html')
def contract(request):
    if request.method=="POST":
        name = request.POST['name']
        email = request.POST['email']
        desc = request.POST['desc']
        values = Contract(name=name, email=email, desc=desc)
        values.save()
    return render(request, 'contract.html')

    






















# def add(request):
#     num1 = int(request.GET['num1'])
#     num2 = int(request.GET['num2'])

#     result = num1+num2

#     return render(request, 'result.html', {'result': result})



# def home(request):
#     # return HttpResponse("Hello Bro")
#     text = {'name': 'sayeed', 'age': 19}
#     return render(request, 'index.html', text)
   
# def home(request):
#     # return HttpResponse('Hello Sayeed')
#     text = {'name': 'jakirul', 'age': 20}
#     return render(request, 'index.html', text)