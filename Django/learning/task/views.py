from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm
from django.http import HttpResponseNotFound

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task/task_list.html', {'tasks': tasks})

def task_add(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'task/task_form.html', {'form': form, 'action': 'Add'})

def task_update(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'task/task_form.html', {'form': form, 'action': 'Update'})

def task_delete(request, task_id):
    try:
        task = Task.objects.get(id=task_id)
        task.delete()
        return redirect('task_list')
    except Task.DoesNotExist:
        return HttpResponseNotFound("Task not found")
