from django.urls import path
from .views import list_todo

urlpatterns = [
    path("list",list_todo,name="my_todo_list")
  
]
