from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm

def index_view(request):

    tasks = Task.objects.all()

    context = {
        'tasks':tasks,
        'form':TaskForm
    }

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect(to='index')

    return render(request, template_name='tasks/index.html', context=context)

def update_task_view(request, task_id):

    task = Task.objects.get(id=task_id)
    form = TaskForm(instance=task)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            
            return redirect(to='index')
    
    context = {
        'form':form
    }
    return render(request, template_name='tasks/update_task.html', context=context)


def delete_task_view(request, task_id):
    
    task = get_object_or_404(Task, pk=task_id)

    if request.method == 'POST':
        task.delete()
        return redirect(to='index')
        
    context = {
        'task':task
    }
    return render(request, template_name='tasks/delete_task.html', context=context)