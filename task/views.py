from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404

from task.models import Task


def tasks(request):
    tasks = Task.objects.all()
    print(tasks)
    return render(request, 'task/tasks.html', context={'tasks': tasks})


def task_detail(request, id):
    task = Task.objects.get(id=id)
    return render(request, 'task/task_detail.html', context={'task': task})


# Create your views here.
def create_task(request):
    if request.method == "POST":
        name = request.POST.get('name')
        status = request.POST.get('status')
        created_by_id = request.POST.get('created_by')

        user = User.objects.get(id=created_by_id)

        Task.objects.create(
            name=name,
            status=status,
            created_by=user
        )

        return redirect('tasks')

    users = User.objects.all()
    return render(request, 'task/create_task.html', {'users': users})


def update_task(request, id):
    task = get_object_or_404(Task, id=id)

    if request.method == "POST":
        task.name = request.POST.get('name')
        task.status = request.POST.get('status')
        created_by_id = request.POST.get('created_by')

        user = User.objects.get(id=created_by_id)
        task.created_by = user

        task.save()
        return redirect('tasks')

    users = User.objects.all()
    return render(request, 'task/update_task.html', {'task': task, 'users': users})


def delete_task(request, id):
    task = Task.objects.filter(id=id)
    tasks = Task.objects.all()
    if task:
        task.delete()

        return render(request, 'task/tasks.html' , context={'tasks': tasks})

    return render(request, 'task/tasks.html', context={'tasks': tasks})
