from django.shortcuts import render, redirect
from projects.models import Project
from django.contrib.auth.decorators import login_required
from projects.forms import ProjectForm


@login_required
def list_projects(request):
    projects = Project.objects.filter(owner=request.user)
    context = {
        "projects": projects,
    }
    return render(request, "project/projects_list.html", context)


@login_required
def show_project(request, id):
    detail = Project.objects.get(id=id)
    context = {
        "project_object": detail,
    }
    return render(request, "project/detail.html", context)


@login_required
def create_project(request):
    form = ProjectForm(request.POST)
    if form.is_valid():
        project = form.save(False)
        project.owner = request.user
        project.save()
        return redirect("list_projects")
    else:
        form = ProjectForm()
    context = {"form": form}
    return render(request, "project/create.html", context)
