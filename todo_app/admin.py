from django.contrib import admin
from .models import Todo

class TodoCustomize(admin.ModelAdmin):
    list_display=['title','description','status','user','image']

admin.site.register(Todo,TodoCustomize)





