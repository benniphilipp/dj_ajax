from django.db import models
from django.contrib.auth.models import User

from profiles.models import Profile

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    liked = models.ManyToManyField(User, blank=True)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    update = models.DateTimeField(auto_now=True)
    create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    @property
    def like_count(self):
        return self.liked.all().count()
    
    def get_photos(self):
        return self.photo_set.all()

    class Meta:
        ordering = ("-create",)

class Photo(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="photos")
    create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.post.title}-{self.pk}"