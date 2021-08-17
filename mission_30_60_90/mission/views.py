from django.db.models import fields
from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.views.generic import CreateView, ListView
from .models import Missions,Status
from datetime import date
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

class MissionListView(LoginRequiredMixin,ListView):
    model = Missions
    template_name = 'mission/user_missions.html'
    context_object_name = 'missions'

    def get_queryset(self):
        user = get_object_or_404(User,username=self.kwargs.get('username'))
        return Missions.objects.filter(aspirant=user).order_by('-start_date')      

def missiontoday(request,**kwargs):
    
    mission = get_object_or_404(Missions,mission_name=kwargs.get('mission_name'))
    dayno = (date.today()-mission.start_date).days
    dayno+=1
    print(dayno)
    status = Status.objects.filter(mission_id=mission.id,day_no=dayno)
    print(len(status))
    return render(request,'mission/mission_today.html',{'status':status})