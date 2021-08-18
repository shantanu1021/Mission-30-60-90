from django.db.models import fields
from django.db.models.base import Model
from django.shortcuts import get_list_or_404, get_object_or_404, render,redirect
from django.views.generic import CreateView, ListView
from django.contrib import messages
from .models import Missions,Status
from datetime import date
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from .forms import StatusUpdateForm
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
    status = Status.objects.filter(mission_id=mission.id,day_no=dayno)
    
    if len(status)==0:
        pass
    else:
        status=status[0]
    
    if request.method == 'POST':
        form = StatusUpdateForm(request.POST, instance=status)

        if form.is_valid():
            form.save()
            messages.success(request,f'Status updated')
            return redirect('mission-home')
    else:
        form = StatusUpdateForm(instance=request.user)

    context={
        'status':status,
        'form':form,
        'mission_name':mission.mission_name
    }
    
    return render(request,'mission/mission_today.html',context)

def statuslist(request,**kwargs):
    
    mission = get_object_or_404(Missions,mission_name=kwargs.get('mission_name'))   
    statuses = Status.objects.filter(mission_id=mission.id)
    dayno = (date.today()-mission.start_date).days
    dayno+=1  
    context={
        'statuses':statuses,
        'dayno':dayno,
        'mission_name':mission.mission_name
    }
    
    return render(request,'mission/status_list.html',context)    