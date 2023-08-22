from django.shortcuts import render
from .models import Todo 
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# login required
@login_required
def list_todo(request):

    # SQL query
    #select * from table_name;
    my_user = request.user
    # ORM Query
    todo_list = Todo.objects.filter(user=my_user)
    
    data = {
        'todo_list_show':todo_list
    }
    
    return render(request,"todo/index.html",data)    

@login_required
def create_todo(request):
    if request.method=="POST":
        # data - title description
        data_title = request.POST['xasdfasdf']
        data_description = request.POST['y']
        front_image = request.FILES['my_image']
        print(data_title,data_description)
        my_user = request.user
        
        # which table - Todo
        Todo.objects.create(description=data_description,title=data_title,user=my_user,image=front_image)
        messages.info(request,f"{data_title} has been created...")
        
        
        
       
        
        
    return render(request,"todo/create_todo.html")

@login_required
def delete_todo_method(request,id):
    # delete
    # SQL query
    # select * from todo where id =id;
    # ORM query
    
    obj = Todo.objects.get(id=id) 
    obj.delete()
    messages.info(request,f"Todo has been deleted...")
    todo_list = Todo.objects.all()
    data = {
        'todo_list_show':todo_list
    }
    
    return render(request,"todo/index.html",data)
