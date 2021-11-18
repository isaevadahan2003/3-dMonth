from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    image = models.FileField(upload_to="post_images/")
    likes = models.IntegerField(default=0)
    reposts = models.IntegerField(default=0)
