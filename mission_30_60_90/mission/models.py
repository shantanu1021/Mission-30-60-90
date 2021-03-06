from django.db import models
from datetime import date
from django.contrib.auth.models import User
from django.urls import reverse
from . import validate

class Missions(models.Model):

    mission_name = models.CharField(max_length=50)
    no_of_days = models.IntegerField(validators=[validate.validate_days])
    start_date = models.DateField(default=date.today)
    aspirant = models.ForeignKey(User, on_delete=models.CASCADE)

    
    def __str__(self):
        return self.mission_name
    
    def get_absolute_url(self):
        return reverse('mission-home')
          

class Status(models.Model):

    mission_id = models.ForeignKey(Missions, on_delete=models.CASCADE)
    day_no = models.IntegerField()
    is_done = models.BooleanField(default=False)
    remarks = models.TextField()
    
    def __str__(self):
        return f'{self.mission_id} day {self.day_no}'

