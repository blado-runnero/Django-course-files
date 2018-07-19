from django.db import models

# Create your models here.
class Users(models.Model):
    f_name = models.CharField(max_length=264)
    l_name = models.CharField(max_length=264)
    email = models.EmailField(max_length=70, null=True, blank=True, unique=True)

    def __str__(self):
        return self.f_name+" "+self.l_name
