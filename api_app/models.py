from django.db import models
from django.utils import timezone

# Create your models here.
class Broast(models.Model):
    is_roast = models.BooleanField()
    content = models.CharField(max_length=280)
    up = models.IntegerField(default=0)
    down = models.IntegerField(default=0)
    date = models.DateTimeField(default=timezone.now)
    @property
    def score(self):
        return self.up - self.down