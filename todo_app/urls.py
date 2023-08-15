from django.urls import path
from .views import list_todo,create_todo

urlpatterns = [
    path("list",list_todo,name="my_todo_list"),
    path("create-todo",create_todo,name="create_my_todo")
  
]
