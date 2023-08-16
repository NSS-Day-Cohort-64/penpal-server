from django.db import models

class LetterTag(models.Model):
    letter = models.ForeignKey("Letter", on_delete=models.DO_NOTHING)
    tag = models.ForeignKey("Tag", on_delete=models.DO_NOTHING)
