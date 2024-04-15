from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Todo
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def homePage(request):
    if request.method == "POST":
        task = request.POST.get('task')
        newTodo = Todo(user=request.user, todoName=task, status=False)
        newTodo.save()
        return redirect('home-page')
    
    all_todos = Todo.objects.filter(user=request.user)
    context = {
        'todos' : all_todos,
    }

    return render(request, 'todoapp/todo.html', context)

def register(request):
    if  request.method == "POST":
        userName = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if len(password) < 6:
            messages.error(request, "Password must be at least 6 characters")
            return redirect('register')
        
        get_all_users_by_username  = User.objects.filter(username=userName).exists()
        if get_all_users_by_username:
            messages.error(request, "Username already exists")
            return redirect('register')

        newUser = User.objects.create_user(username=userName, email=email, password=password)
        newUser.save()

        messages.success(request, "User successfully created, Login now")
        redirect('login')

    return render(request,'todoapp/register.html', {})

def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get( 'username' )
        password = request.POST.get( 'password' )
        user = authenticate(username=username, password=password)
        if user is not None :
            login(request, user)
            messages.info(request,"You are  now logged in.")
            return redirect("home-page")
        else:
            messages.error(request, "Invalid username or password!")
    return render(request, 'todoapp/login.html', {})

def logoutView(request):
    logout(request)
    return redirect('login')

def deleteTask(request, id):
    taskToDelete = Todo.objects.get(user=request.user, my_id=id)
    taskToDelete.delete()
    return redirect('home-page')

def updateTask(request, id):
    taskToUpdate = Todo.objects.get(user=request.user, my_id=id)
    taskToUpdate.status = True
    taskToUpdate.save()
    return redirect('home-page')