from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from taggit.managers import TaggableManager
from django.urls import reverse
from django.contrib.auth import get_user_model
from datetime import date

User = get_user_model()

class Company(models.Model):
    name = models.CharField(max_length=500)
    description = RichTextUploadingField()
    logo = models.ImageField(
        upload_to="jobs/companylogos",
        blank=True,
        null=True,
    )
    website = models.CharField(max_length=100, default="")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "company"
        verbose_name_plural = "companies"


class Job(models.Model):
    
    JOB_TYPE = (("1", "Full time"), ("2", "Part time"), ("3", "Internship"))

    title = models.CharField(max_length=300)
    description = RichTextUploadingField()
    host = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=150)
    type = models.CharField(choices=JOB_TYPE, max_length=10)
    last_date = models.DateField()
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, null=True, blank=True
    )
    link = models.CharField(max_length=500, default="", blank=True, null=True,help_text="Your google form link")
    created = models.DateTimeField(auto_now_add=True)
    salary = models.CharField(max_length=8, blank=True)
    tags = TaggableManager()

    class Meta:
        ordering = ["-created"]

    def get_absolute_url(self):
        return reverse("jobs:jobs-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.title
    
    @property
    def is_past_due_date(self):
        return date.today() > self.last_date


# class Applicant(models.Model):
#     user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
#     job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name="applicants")
#     created = models.DateTimeField(auto_now_add=True)
#     status = models.SmallIntegerField(default=1)

#     class Meta:
#         ordering = ["id"]
#         unique_together = ["user", "job"]

#     def __str__(self):
#         return self.user.get_full_name()

#     @property
#     def get_status(self):
#         if self.status == 1:
#             return "Pending"
#         elif self.status == 2:
#             return "Accepted"
#         else:
#             return "Rejected"
