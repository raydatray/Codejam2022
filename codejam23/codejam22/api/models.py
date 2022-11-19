from django.db import models

# Create your models here.


class listing(models.Model):
    userName = models.CharField(max_length=100)
    scheduleTime = models.TimeField()
    createdTime = models.TimeField(auto_now=True)

    def __str__(self):
        return self.userName
