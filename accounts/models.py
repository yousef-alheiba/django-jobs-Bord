from django.db import models
from django.contrib.auth.models import User
# Create your models here.

Citys = (
    ('Amman','Amman'),
    ('Alzrqa','Alzrqa'),
    ('Erbad','Erbad'),
)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city= models.ForeignKey(User, verbose_name="Citys", on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=10)
    image = models.ImageField(upload_to='profile/')

    def __str__(self):
        pass
