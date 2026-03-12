from django.db import models
from django.contrib.auth.models import User

class ImageUpload(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    result = models.CharField(max_length=50)
