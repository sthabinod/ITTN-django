from django.shortcuts import render
from .models import Todo 

def list_todo(request):
    # logic
    
    # SQL query
    # select * from todo where id=1;
    
    # ORM query
    todo_list = Todo.objects.all()
    
    data = {
        'todo_list_all':todo_list
    }
   
    return render(request,"todo/index.html",data)    