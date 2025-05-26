from django import forms
from .models import Presupuesto

class PresupuestoForm(forms.ModelForm):
    class Meta:
        model = Presupuesto
        fields = ['nombre', 'email', 'mensaje']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Tu nombre',
                'required': True,
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-input',
                'placeholder': 'tu@email.com',
                'required': True,
            }),
            'mensaje': forms.Textarea(attrs={
                'class': 'form-textarea',
                'placeholder': 'Escribe tu solicitud aquí...',
                'rows': 5,
                'required': True,
            }),
        }
