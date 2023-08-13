from django.shortcuts import render
from .models import Todo 

def list_todo(request):
    # logic
    # select * from todo_app_todo;
    # ORM - object relational mapper
    # list
    
    todo_list = Todo.objects.all() 
    print(todo_list)
    data = {
        'todo_list_data':todo_list
    }
    return render(request,"todo/index.html",data)    