from .models import Job, Company
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .form import JobCreateForm,CompanyCreateForm
from django.http import Http404



def job_list(request):
    jobs = Job.objects.all()
    # colors = ["badge alert-success","badge alert-danger","badge alert-info"]
    paginator = Paginator(jobs, per_page=6)
    page_number = request.GET.get("page", 1)
    all_jobs = paginator.page(page_number)
    return render(request, "jobs/job_list.html", {"jobs": all_jobs})


@login_required
def detailed_job(request, pk):
    try:
        job = get_object_or_404(Job, id=pk)
    except Exception as e:
        raise e

    return render(request, "jobs/detailed_job.html", {"job": job})


@user_passes_test(lambda u: u.is_staff)
def create_job(request):
    form = JobCreateForm()
    # process data from form
    if request.method == "POST":
        form = JobCreateForm(request.POST)
        if form.is_valid():
            # the below line will save the form data in model Room
            form.instance.host = request.user
            form.save()
            return redirect("jobs")
    context = {"form": form}
    return render(request, "jobs/job_form.html", context)

@user_passes_test(lambda u: u.is_staff)
def create_company(request):
    form = CompanyCreateForm()
    # process data from form
    if request.method == "POST":
        form = CompanyCreateForm(request.POST)
        if form.is_valid():
            # the below line will save the form data in model Company
            form.save()
            return redirect("createjob")
    context = {"form": form}
    return render(request, "jobs/company_form.html", context)


@user_passes_test(lambda u: u.is_staff)
def update_job(request, pk):
    job = Job.objects.get(id=pk)
    form = JobCreateForm(instance=job)
    if request.method == "POST":
        form = JobCreateForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            return redirect("jobs-detail",pk)
    context = {"form": form}
    return render(request, "jobs/job_form.html", context)

@user_passes_test(lambda u: u.is_staff)
def delete_job(request, pk):
    data = get_object_or_404(Job, id=pk)
    if data.host == request.user:
        data.delete()
        return redirect('home')
    else:
        raise Http404