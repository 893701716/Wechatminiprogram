from django.db import models

# Create your models here.
class Music(models.Model):
    name = models.CharField(max_length=50)
    music = models.FileField(upload_to='music/')
    created = models.DateTimeField(auto_now_add=True)

    def __self__(self):
        return self.name
