from django.db import models
from django.conf.urls.static import static
import re

# Create your models here.

class Track(models.Model):
    file = models.FileField(upload_to="stream/audio")

    def __str__(self):
        return re.split(r".*\/", self.file.name)[1]