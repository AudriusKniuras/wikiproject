from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'entryapp/index.html')

def aws(request):
    return render(request, 'entryapp/aws.html')

def python(request):
    return render(request, 'entryapp/python.html')

def network(request):
    return render(request, 'entryapp/network.html')

def linux(request):
    return render(request, 'entryapp/linux.html')

def about(request):
    return render(request, 'entryapp/about.html')