from django.db import models
from user.models import CustomUser


class Note(models.Model):
    note_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE)
    title = models.TextField()
    text = models.TextField()
    url = models.CharField(max_length=100, blank=True)
    isPublic = models.BooleanField(default=False)

    def __str__(self):
        return self.title
