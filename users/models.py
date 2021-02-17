from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.

class Profile(models.Model):
    #creating a one to one reletionship with a particuler user
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #creating image filed
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        #showing what a user can see on his profile
        return f"{self.user.username} Profile" 


    # image auto resize
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300 , 300)
            img.thumbnail(output_size)
            img.save(self.image.path)







