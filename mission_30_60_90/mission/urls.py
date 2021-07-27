from django.urls import path
from . import views

urlpatterns= [
    path('',views.home,name='mission-home'),
    path('about/',views.about,name='mission-about'),
]