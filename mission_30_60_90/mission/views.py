from django.db.models import fields
from django.shortcuts import render
from django.views.generic import CreateView
from .models import Missions,Status
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
# Create your views here.
def home(request):
    return render(request,'mission/home.html')

def about(request):
    return render(request,'mission/about.html',{'title':'About'})    

class MissionCreateView(LoginRequiredMixin,CreateView):
    model = Missions
    fields = ['mission_name','no_of_days']

    def form_valid(self,form):
        form.instance.aspirant = self.request.user
        return super().form_valid(form)