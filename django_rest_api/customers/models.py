from django.db import models

# Create your models here.
class Customers(models.Model):
    name=models.CharField(max_length=50)
    code=models.CharField(max_length=8)
    is_regular = models.BooleanField(default=False)

    def __str__(self):
        return self.name