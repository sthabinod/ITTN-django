from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout
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
    
    # Check request method
    if request.method == 'POST':
        # get frontend username and password
        front_username = request.POST['username'] #binod
        front_password = request.POST['password']
        
        print(front_username, front_password)

        # Checking if the user exists in database
        if User.objects.filter(username=front_username).exists():
            messages.error(request, 'User already exists!')
        else:
            User.objects.create(username=front_username,password=front_password)
            # user create
            messages.info(request, 'User created Successfully!')
            
    else:
        print("This is not POST method")
    
    
    return render(request,"registration.html")


def logout_user(request):
    logout(request)
    return redirect('login_user')