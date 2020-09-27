from django.db import models


# Create your models here.
class Contact(models.Model):
    sn0 = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255,blank=True)
    phone = models.CharField(max_length=13)
    email = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return 'Message from ' + self.name 

# Create your models here.

