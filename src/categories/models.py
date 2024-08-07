from django.db import models

# Create your models here.

from django.db import models

# Create your models here.


# folders/models.py

from django.db import models

from kuila import settings


class Category(models.Model):
    name = models.CharField(max_length=200)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

