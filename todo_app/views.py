from django.shortcuts import render

def list_todo(request):
    # logic
    return render(request,"todo/index.html")