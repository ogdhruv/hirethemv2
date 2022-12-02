from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth import get_user_model

User = get_user_model()

class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.CASCADE)
    # company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = RichTextUploadingField()
    participants = models.ManyToManyField(
        User, related_name="participants", blank=True
    )
    image = models.ImageField(
        upload_to="room/photos/",
        blank=True,
        null=True
    )

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    tags = TaggableManager()

    class Meta:
        ordering = ["-updated"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("room_detail", kwargs={"pk": self.pk})


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body
