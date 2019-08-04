from django.db import models
from django.conf.urls.static import static

# Create your models here.

class Track(models.Model):
    file = models.FileField(upload_to="stream/audio")