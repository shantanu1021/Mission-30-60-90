from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'mission/home.html')

def about(request):
    return render(request,'mission/about.html',{'title':'About'})    