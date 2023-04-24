from django.shortcuts import render, redirect
from .models import Tareas, get_current_user
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from .forms import TareasForm

@login_required
def page(request):
    if request.method == 'POST':
        form = TareasForm(request.POST)
        if form.is_valid():
            tarea = form.save(commit=False)
            tarea.user = request.user
            tarea.save()
            return redirect('todolist')
    else:
        tasks = Tareas.objects.all()
        user_tasks = Tareas.objects.filter(user=request.user)
        form = TareasForm()
        context = {
            'user_tasks': user_tasks,
            'tasks': tasks,
            'form': form,
        }
        return render(request, 'tasks.html', context)

@login_required(login_url='login_todolist')
def mi_vista(request):
    username = request.user.username
    email = request.user.email
    tareas = Tareas.objects.filter(user=request.user)
    return render(request, 'todolist.html', {
        'username': username,
        'email': email,
        'tareas': tareas
    })

@login_required(login_url='login_todolist')
def list_routines(request):
    db_data = Tareas.objects.filter(user=request.user)
    context = {
        "db_data": db_data[::-1],
        "update": None
    }
    return render(request,'todolist/todolist.html', context)

@login_required
def insert_tarea(request):
    try:
        tareas_subject = request.POST['subject']
        tareas_description = request.POST['description']
        tareas_is_done = 'is_done' in request.POST
        # tareas_is_done = request.POST.get('is_done', False)

        if tareas_subject == "" or tareas_description == "":
            raise ValueError("Invalid subject text vacio")

        db_data = Tareas(subject=tareas_subject, description=tareas_description, is_done=tareas_is_done, user=get_current_user(request))
        db_data.save()
        return redirect('todolist')
    except ValueError as error:
        print(error)
        return render(request,'todolist/todolist.html')

def delete(request, tarea_id):
    db_data  = Tareas.objects.filter(id=tarea_id)
    db_data.delete()
    return HttpResponseRedirect(reverse('todolist'))

def update(request):
    tarea_id = request.POST['id']
    tarea_subject = request.POST['subject']
    tarea_description = request.POST['description']
    db_data = Tareas.objects.get(pk=tarea_id)
    db_data.subject = tarea_subject
    db_data.description = tarea_description
    db_data.save( )
    return HttpResponseRedirect(reverse('todolist'))

def update_form(request, tarea_id):
    db_data = Tareas.objects.all()
    db_data_only = Tareas.objects.get(pk=tarea_id)
    context = {
        "db_data": db_data[::-1],
        "update": db_data_only
    }
    return render(request,'todolist/create_routine.html', context)

def register_todolist(request):
    if request.user.is_authenticated:
        return redirect('web')
    else:
        register_form = RegisterForm()

        if request.method == 'POST':
            register_form = RegisterForm(request.POST)

            if register_form.is_valid():
                register_form.save()
                messages.success(request, 'Te has registrado correctamente!!!')
                
                return redirect('todolist')

        return render(request, 'todolist/register_todolist.html', {
            'title': 'Registro',
            'register_form': register_form
        })
 
@login_required
def create_routine(request):
    if request.method == 'POST':
        form = TareasForm(request.POST)
        if form.is_valid():
            tarea = form.save(commit=False)
            tarea.user = get_current_user(request)
            tarea.save()
            return redirect('tareas_list')
    else:
        form = TareasForm()
    return render(request, 'todolist/create_routine.html', {'form': form})

def login_todolist(request):
    if request.user.is_authenticated:
        return redirect('web')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.info(request, "Has iniciado sesión correctamente")
                return redirect('todolist')
                

            else:
                messages.warning(request, 'No te has podido identificar correctamente intenta de nuevo mas tarde!!!')
        return render(request, 'todolist/login_todolist.html', {
            'title': 'Identificate',
        })

def logout_todolist(request):
    logout(request)

    return redirect('login_todolist')