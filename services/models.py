from django.db import models

# Create your models here.
class services_page(models.Model):
    sevices=models.CharField(max_length=150,blank=True,default="")
    ervices_heder=models.CharField(max_length=100,blank=True,default="")
    ervices_heders=models.CharField(max_length=100,blank=True,default="")



class homepage_box(models.Model):
    box_header=models.CharField(max_length=100,blank=True,default="")
    photo=models.ImageField(blank=True,default="")


class homepage_banner(models.Model):
    banner=models.CharField(max_length=700)
  


class homepage_box2(models.Model):
    box_header=models.CharField(max_length=100,blank=True,default="")
    sevices=models.CharField(max_length=150,blank=True,default="")


class footer(models.Model):
    title=models.CharField(max_length=300,blank=True,default="")
    facbook=models.URLField(null=True, blank=True, max_length=200)
    twitter=models.URLField(null=True, blank=True ,max_length=200)
    instagram=models.URLField(null=True, blank=True ,max_length=200)
    youtube=models.URLField(null=True, blank=True ,max_length=200)
    linkdin=models.URLField(null=True, blank=True ,max_length=200)
    github=models.URLField(null=True, blank=True ,max_length=200)


    def get_social_links(self):
        return [
            ("Facebook", self.facbook),
            ("Twitter", self.twitter),
            ("Instagram", self.instagram),
            ("YouTube", self.youtube),
            ("LinkedIn", self.linkdin),
            ("GitHub", self.github),
        ]

class class_routine(models.Model):
    titel=models.CharField(max_length=100)
    photo=models.ImageField()         

