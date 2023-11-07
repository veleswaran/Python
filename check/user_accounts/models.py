from django.db import models
from django.contrib.auth.models import User
import user_accounts

# Create your models here.

class dailytopic(models.Model):
    topic = models.CharField(max_length=100)
    activity = models.TextField()
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='images/' ,null=True)
