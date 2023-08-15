from django.shortcuts import render
from .models import Todo 

def list_todo(request):

    # SQL query
    #select * from table_name;
    
    # ORM Query
    todo_list = Todo.objects.all()
    
    data = {
        'todo_list_show':todo_list
    }
    
    return render(request,"todo/index.html",data)    


def create_todo(request):
    
    if request.method=="POST":
        # data - title description
        data_title = request.POST['my_title']
        data_description = request.POST['my_description']
        print(data_title,data_description)
        
        # which table - Todo
        Todo.objects.create(title=data_title,description=data_description)
    
    return render(request,"todo/create_todo.html")