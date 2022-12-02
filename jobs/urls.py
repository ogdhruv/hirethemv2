from django.urls import path, include
from .views import job_list, detailed_job, create_job,create_company,update_job

urlpatterns = [
    path("", view=job_list, name="jobs"),
    path("?=<int:pk>/", view=detailed_job, name="jobs-detail"),
    path("?=<int:pk>/update", view=update_job,name="updatejob"),
    path("createjob/", view=create_job, name="createjob"),
    path("createcompany/", view=create_company, name="createcompany"),
]
