from django.db import models

class Tag(models.Model):
    label = models.CharField(max_length=25)
    date_created = models.DateField(auto_now=True)
