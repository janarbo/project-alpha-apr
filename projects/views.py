from django.shortcuts import render, get_object_or_404
from projects.models import Project
from django.contrib.auth.decorators import login_required


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
