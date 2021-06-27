from django.db import models
from datetime import date

# Create your models here.

class contacts(models.Model):
    message_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    message = models.CharField(max_length=300)
    email = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class user(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=13)
    email = models.EmailField()
    password = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name} {self.email}'
    
    def isExists(self):
        if user.objects.filter(email=self.email):
            return True
        return False

class posts(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    post = models.CharField(max_length=5000)
    dated = models.DateField(default=date.today)

    def __str__(self):
        return f'{self.name} {self.dated}'