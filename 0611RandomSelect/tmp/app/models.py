from django.db import models

# Create your models here.
class UserRecord(models.Model):
    username = models.CharField(max_length=128)
    address = models.CharField(max_length=128)

    def __str__(self):
        return self.username+'-'+self.address

