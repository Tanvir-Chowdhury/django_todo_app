from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.

def index(request):
    if request.method == 'POST':
        title = request.POST.get("title")
        description = request.POST.get("description")
        task = Todo.objects.create(title = title, description = description)
        task.save()
    item_list = Todo.objects.all().order_by('-date')
    return render(request, 'index.html',{'item_list' : item_list})
        

def remove_task(request, task_id):
    task = Todo.objects.get(id = task_id)
    task.delete()
    return redirect('home')
