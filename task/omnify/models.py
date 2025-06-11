from django.db import models
from django.contrib.auth.models import AbstractUser

class Customuser(AbstractUser):
    STATUS_ROLE=[
        ('client','Client'),
        ('instructor','Instructor')
    ]
    role=models.CharField(max_length=15,choices=STATUS_ROLE,null=True,blank=True)


class FitnessClass(models.Model):
    name=models.CharField(max_length=150,null=True,blank=True,db_index=True)
    date_time=models.DateTimeField(null=True,blank=True)
    instructor=models.ForeignKey(Customuser,on_delete=models.CASCADE,related_name='fitnessinstructor')
    available_slots=models.IntegerField(null=True,blank=True)

    def __str__(self):
        return f'Fitness Class Created By {self.instructor.username}.'

class Request(models.Model):
    class_id=models.ForeignKey(FitnessClass,on_delete=models.CASCADE,related_name='requests')
    client_name=models.ForeignKey(Customuser,on_delete=models.CASCADE,related_name='customuser_client')
    client_email=models.ForeignKey(Customuser,on_delete=models.CASCADE,related_name='client_email')
    booked_slot=models.IntegerField(null=True,blank=True)
    
    def __str__(self):
        return f'Requested By {self.client_name.username}.'
