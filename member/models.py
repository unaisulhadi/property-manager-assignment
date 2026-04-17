from django.db import models

# Create your models here.


class Member(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.full_name
