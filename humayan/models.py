from django.db import models

# Create your models here.
class registrations(models.Model):
    Name= models.CharField(blank=False,null=False,max_length=50)
    Email=models.EmailField(blank=False,null=False,unique=True)
    Pass= models.CharField(blank=False,null=False,max_length=12)
    Repass=models.CharField(blank=False,null=False,max_length=12)
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True, null=True)