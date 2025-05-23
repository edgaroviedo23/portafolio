from django import forms
from .models import Comentario, Presupuesto

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['nombre', 'contenido']

class PresupuestoForm(forms.ModelForm):
    class Meta:
        model = Presupuesto
        fields = ['nombre', 'email', 'mensaje']

class PresupuestoForm(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-input',
        'placeholder': 'Tu nombre',
        'required': True
    }))
    email = forms.EmailField(label='Correo Electrónico', widget=forms.EmailInput(attrs={
        'class': 'form-input',
        'placeholder': 'tu@email.com',
        'required': True
    }))
    mensaje = forms.CharField(label='Mensaje', widget=forms.Textarea(attrs={
        'class': 'form-textarea',
        'placeholder': 'Escribe tu solicitud aquí...',
        'rows': 5,
        'required': True
    }))
