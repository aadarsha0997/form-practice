from django.db import models

# Create your models here.

class UserProfile(models.Model):
   # image=models.FileField(upload_to="images")
    image=models.ImageField(upload_to="images") #only images are now valid to uplode no any pdf/txt file in allowerd with this field.