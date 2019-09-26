from django.db import models
from django.utils import timezone
from django.core.validators import MinLengthValidator


class Inote(models.Model):
    title = models.CharField('title', max_length=50)
    text = models.TextField('text', max_length=200, blank=False, validators=[MinLengthValidator(50)])
    date = models.DateTimeField('date', default=timezone.now())

