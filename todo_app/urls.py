from django.urls import path
from .views import list_todo,create_todo,delete_todo_method
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("list",list_todo,name="my_todo_list"),
    path("create-todo",create_todo,name="create_my_todo"),
    path("delete-my-todo/<int:id>",delete_todo_method,name="delete_todo")
  
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)