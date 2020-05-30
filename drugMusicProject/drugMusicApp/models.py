from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length = 15)
    category = models.SmallIntegerField(null=True)
    image = models.ImageField()
    detail = models.TextField()
    place = models.CharField(max_length = 20)
    line = models.CharField(max_length = 20)
    post_date = models.DateTimeField(auto_now_add=True)

class Video(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="videos")
    link = models.CharField(max_length=100)