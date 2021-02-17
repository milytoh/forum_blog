from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse



# Create your models here.

class Post(models.Model):
    #creating post atributes
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    #date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    liked = models.ManyToManyField(User, default=None, blank=True, related_name='liked')
    
    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('myblog:post-detail', kwargs={'pk': self.pk})



    @property
    def num_likes(self):
        return self.liked.all().count()

Like_choices = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike'),

    )

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    values = models.CharField(choices=Like_choices, default="Like", max_length=10)

    def __str__(self):
        return str(self.post)



        