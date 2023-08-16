from django.urls import path
from .views import list_todo,create_todo,delete_todo_method

urlpatterns = [
    path("list",list_todo,name="my_todo_list"),
    path("create-todo",create_todo,name="create_my_todo"),
    path("delete-my-todo/<int:id>",delete_todo_method,name="delete_todo")
  
]
