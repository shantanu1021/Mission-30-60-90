from django.urls import path
from . import views
from .views import MissionCreateView,MissionListView

urlpatterns= [
    path('',views.home,name='mission-home'),
    path('mission/new/',MissionCreateView.as_view(),name='mission-create'),
    path('mission/<str:mission_name>/',views.missiontoday,name='mission-today'),
    path('user/<str:username>',MissionListView.as_view(),name='user-missions'),
    path('about/',views.about,name='mission-about'),
]