from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Album(models.Model):
    artist_name=models.CharField(max_length=150)
    album_icon=models.FileField(max_length=150)
    genre=models.CharField(max_length=50)
    album_name=models.CharField(max_length=150)

    def get_absolute_url(self):
        return reverse('music:details',kwargs={'pk':self.pk})

    def __str__(self):
        return self.artist_name + "-" + self.album_name

class Song(models.Model):
    album_name = models.ForeignKey(Album,on_delete=models.CASCADE)
    file_type = models.CharField(max_length=50)
    file_name = models.CharField(max_length=50)
    is_fav = models.BooleanField(default=False)
    song_choose =models.FileField(max_length=100 ,default=False)
    def __str__(self):
        return self.file_name
    def get_absolute_url(self):
        return reverse('music:index')