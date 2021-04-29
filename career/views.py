from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')

def oncampus(request):
    return render(request, 'on-campus.html')

def offcampus(request):
    return render(request, 'off-campus.html')

def intern(request):
    return render(request, 'intern.html')