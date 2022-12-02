from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.conf import settings
from django.urls import reverse
from taggit.managers import TaggableManager

class Post(models.Model):
    title = models.CharField(max_length=500)
    slug = models.CharField(max_length=150)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="blog_post"
    )
    thumbnail =  models.ImageField(
        upload_to="photos/profiles",
        default="defaults/blog/default.jpg",
        blank=True,
        null=True
    )

    body = RichTextUploadingField()
    tags = TaggableManager()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created"]

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse("blog_detail", kwargs={"pk": self.pk})
