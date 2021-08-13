from django.urls import path
from . import views
from .views import MissionCreateView

urlpatterns= [
    path('',views.home,name='mission-home'),
    path('mission/new/',MissionCreateView.as_view(),name='mission-create'),
    path('about/',views.about,name='mission-about'),
]