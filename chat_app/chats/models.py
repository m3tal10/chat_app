from django.db import models

# Create your models here.
class Message(models.Model):
    room_name= models.CharField(max_length=255)
    message= models.TextField()
    # sender= models.ForeignKey('User', on_delete= models.CASCADE)
