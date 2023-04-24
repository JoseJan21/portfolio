# from django.shortcuts import render
# from .forms import ContactForm
#CHAT
from django.shortcuts import render, redirect
from .forms import ContactFormForm
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib import messages


def home(request):
    return render(request, 'home.html', {
        'title': 'Inicio',
    })

#CHAT 

def contact(request):
    if request.method == 'POST':
        form = ContactFormForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/gracias/')
    else:
        form = ContactFormForm()
    return render(request, 'contact.html', {'form': form})
# def contact(request):
#     return render(request, 'contact.html')

def email(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        template = render_to_string('email_template.html', {
        'name': name,
        'email': email,
        'message': message
        })

        email = EmailMessage(
            subject,
            template,
            settings.EMAIL_HOST_USER,
            ['josejan303@gmail.com']
        )

        email.fail_silently = False
        email.send()

        messages.success(request, 'se ha enviado tu correo')
        return redirect('mail')

def mail(request):
   return render(request, 'sent_mail.html', {
        'title': 'Inicio',
    })

