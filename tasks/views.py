from django.shortcuts import render, redirect
from tasks.forms import TaskForm
from django.contrib.auth.decorators import login_required
from tasks.models import Task
from django.views.generic import ListView

@login_required
def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            task.owner = request.user
            task.save()
            return redirect("list_projects")
    else:
        form = TaskForm()
        context = {"form": form}
        return render(request, "tasks/create_task.html", context)


@login_required
def show_my_tasks(request):
    task = Task.objects.filter(assignee=request.user)
    context = {"show_tasks": task}
    return render(request, "tasks/show_tasks.html", context)
