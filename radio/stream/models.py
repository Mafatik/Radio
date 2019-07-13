from django.db import models

# Create your models here.


class Playlist(models.Model):
    name = models.CharField(max_length=30)
    genres = models.CharField(max_length=30)
    logo = models.CharField(max_length=1000)

    def __str__(self):
        return self.name + " (" + self.genres + ")"


class Track(models.Model):
    title = models.CharField(max_length=30)
    artist = models.CharField(max_length=30)
    album = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)

    def __str__(self):
        return self.artist + " -- " + self.title
