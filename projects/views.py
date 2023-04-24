from django.shortcuts import render, redirect
import random
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


from .forms import RegisterForm
 # Create your views here.

def generator(request):
    return render(request, 'generator/generator.html')

def password(request):

    characters = list('abcdefghijklmnñopqrstuvwxyz')
    generated_password = ''

    length = int(request.GET.get('length'))

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()+=~-_=+?/><\|'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))


    for x in range(length):
        generated_password += random.choice(characters)

    return render(request, 'generator/password.html', {'password': generated_password})

def web(request):
    return render(request, 'pagina/pagina.html')

def register_page(request):
    if request.user.is_authenticated:
        return redirect('web')
    else:
        register_form = RegisterForm()

        if request.method == 'POST':
            register_form = RegisterForm(request.POST)

            if register_form.is_valid():
                register_form.save()
                messages.success(request, 'Te has registrado correctamente!!!')
                
                return redirect('web')

        return render(request, 'users/register.html', {
            'title': 'Registro',
            'register_form': register_form
        })

def login_page(request):
    if request.user.is_authenticated:
        return redirect('web')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.info(request, "Has iniciado sesión correctamente", extra_tags='blog')
                return redirect('list_articles')
                

            else:
                messages.warning(request, 'No te has podido identificar correctamente intenta de nuevo mas tarde!!!')
        return render(request, 'users/login.html', {
            'title': 'Identificate',
        })

def logout_page(request):
    logout(request)

    return redirect('login')