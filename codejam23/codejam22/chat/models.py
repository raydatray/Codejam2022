from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class roomHistory(models.Model):
    createdBy = models.ForeignKey(
        User, related_name="roomCreator", on_delete=models.CASCADE
    )
    friend = models.ForeignKey(User, related_name="friend", on_delete=models.CASCADE)
    timeCreated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.createdBy} : {self.friend} : {self.timeCreated}"


class message(models.Model):
    room = models.ForeignKey(
        roomHistory, on_delete=models.CASCADE, related_name="chats"
    )
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sender")
    receiver = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="receiver"
    )
    text = models.CharField(max_length=500)
    time = models.TimeField(auto_now=True)
    seen = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.room} : {self.sender} : {self.receiver} : {self.text}"
