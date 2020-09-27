from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from PIL import Image
from django.urls import reverse




# Create your models here.
class Post(models.Model):
    sn0 = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=255, blank=True)
    name = models.CharField(max_length=100)
    instagram_username = models.CharField(max_length=255, blank=True)
    linkedin = models.CharField(max_length=255, blank=True)
    facebook = models.CharField(max_length=255, blank=True)
    twitter = models.CharField(max_length=255, blank=True)
    Add_Field_Name=models.CharField(max_length=255, blank=True)
    Add_Field_Name_2=models.CharField(max_length=255, blank=True)
    Add_Field_Name_3=models.CharField(max_length=255, blank=True)
    Add_Field_Name_4=models.CharField(max_length=255, blank=True)
    Field_Link=models.CharField(max_length=255, blank=True)
    Field_Link_2=models.CharField(max_length=255, blank=True)
    Field_Link_3=models.CharField(max_length=255, blank=True)
    Field_Link_4=models.CharField(max_length=255, blank=True)
    quora = models.CharField(max_length=255, blank=True)
    website = models.CharField(max_length=255, blank=True)
    slug = models.CharField( max_length=130)
    
    timeStamp = models.DateTimeField(default=timezone.now)
  

    def __str__(self):
        return self.full_name

    def save(self, *args, **kwargs):
        super(Post,self).save(*args, **kwargs)
        
        

    def get_absolute_url(self):
        return reverse('blogPost', kwargs={'pk':self.pk})
    

    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics')

    
    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile,self).save(*args, **kwargs)
        
        

