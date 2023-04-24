from django import forms
from .models import ContactForm

#CHAT
# class ContactFormForm(forms.Form):
#     name = forms.CharField(label='Nombre', max_length=100)
#     email = forms.EmailField(label='Correo electrónico', max_length=100)
#     message = forms.CharField(label='Mensaje', widget=forms.Textarea)

class ContactFormForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ['name', 'email', 'message']

# class ContactForm(forms.Form):
#     name = forms.CharField(
#         label="Nombre", required=True)
#     email = forms.EmailField(
#         label="Email", required=True)
#     content = forms.CharField(
#         label="Contenido", required=True, widget=forms.Textarea())
# class ContactoForm(forms.ModelForm):
#     class Meta:
#         model = ContactoForm
#         fields = '__all__'