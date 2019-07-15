from django.db import models

# Create your models here.

class Playlist(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Track(models.Model):
    audiofile = models.FileField(upload_to="stream/static/stream/audio")
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)

    #from string "blah/blah/blah/music.mp3" returns "music.mp3"
    def __str__(self):
        return self.audiofile.name.rpartition('/')[2]
