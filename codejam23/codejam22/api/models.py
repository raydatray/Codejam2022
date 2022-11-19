from django.db import models

# Create your models here.


class User(models.Model):
    sessionId = models.IntegerField()
    profilePic = models.ImageField(default="default.jpg", upload_to="user_profile")
    request = models.ManyToManyField("self", blank=True, symmetrical=False)

    def __str__(self) -> str:
        return f"{self.id}:{self.profilePic}"


class listing(models.Model):
    userName = models.CharField(max_length=100)
    scheduleTime = models.TimeField()
    createdTime = models.TimeField(auto_now=True)
    userSession = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="creator"
    )
    # bodyPart = models.CharField(max_length=100)

    def __str__(self):
        return self.userName
