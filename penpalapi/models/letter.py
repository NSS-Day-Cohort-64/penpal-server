from django.db import models
from django.contrib.auth.models import User

class Letter(models.Model):
    body = models.CharField(max_length=1000)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='authored')
    recipient = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='received_letters')
    date_created = models.DateField(auto_now=True)
    topic = models.ForeignKey("Topic", related_name="letters", on_delete=models.DO_NOTHING)
    tags = models.ManyToManyField("Tag", through="LetterTag")
