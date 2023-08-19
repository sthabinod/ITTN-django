from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib import messages

def login_user(request):
    if request.method == 'POST':
        #    verify
        # login
         # Getting from post request
        username = request.POST['username']
        password = request.POST['password']
        print(username, password)

        # Checking if the user exists in database
        if User.objects.filter(username=username).exists():
        #    login here
            user_obj = User.objects.get(username=username)
            login(request, user_obj)
            return redirect('my_todo_list')
        else:
            messages.error(request, 'Username or password does not matched!')
    else:
        print("This is not POST method")
    return render(request, 'login.html')

def register(request):
    
    
    
    # check if the user already exists
        # already exists
    
    # if not
        # create user
        # send message
    
    # Check request method
    if request.method == 'POST':
        # get frontend username and password
        username = request.POST['username']
        password = request.POST['password']
        print(username, password)

        # Checking if the user exists in database
        if User.objects.filter(username=username).exists():
            messages.error(request, 'User already exists!')
        else:
            User.objects.create(username=username,password=password)
            # user create
            messages.info(request, 'User created Successfully!')
            
    else:
        print("This is not POST method")
    
    
    return render(request,"registration.html")