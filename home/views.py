from django.shortcuts import render ,redirect
from .models import Todo

# Create your views here.
def index (request):
    result= Todo.objects.all()
    parameters ={
        "result":result
    }
    return render(request,"index.html",parameters)
def home(request):
    return render(request,"home.html")
def add_todo(request):
    if request.method=="POST":
        user_task=request.POST.get("task")
        user_created_at=request.POST.get("created_at")
        new_todo=Todo(task=user_task , created_at=user_created_at)
        new_todo.save()
        return redirect("todo")
    return render(request,"add_todo.html")

def delete_todo(request, todo_id):
    todo=Todo.objects.get(id=todo_id)
    todo.delete()

    return redirect("todo")

def update_todo(request ,todo_id):
    todo= Todo.objects.get(id=todo_id)
    if request.method=="POST":
        user_task=request.POST.get("task")
        user_created_at=request.POST.get("created_at")
        todo.task=user_task
        todo.created_at=user_created_at
        todo.save()

        return redirect("todo")
    parameter={
       'todo':todo
    }
    return render(request,"update.html",parameter)

