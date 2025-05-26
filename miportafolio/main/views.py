from django.shortcuts import render, redirect
from .models import Proyecto, Comentario
from .forms import ComentarioForm, PresupuestoForm
from django.core.mail import send_mail
import requests
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

from django.shortcuts import render

def inicio(request):
    return render(request, 'main/inicio.html')

def solicitar_presupuesto(request):
    return render(request, 'main/presupuesto.html', {'form' : PresupuestoForm()})

def presupuesto(request):
    if request.method == 'POST':
        form = PresupuestoForm(request.POST)
        if form.is_valid():
            send_mail(
                'Solicitud de presupuesto',
                f"Nombre: {form.cleaned_data['nombre']}\nEmail: {form.cleaned_data['email']}\nMensaje: {form.cleaned_data['mensaje']}",
                'tu_email@gmail.com',  # Remitente
                ['destino@ejemplo.com'],  # Destinatario
                fail_silently=False,
            )
            return render(request, 'main/gracias.html')
    else:
        form = PresupuestoForm()
    return render(request, 'main/presupuesto.html', {'form': form})



def edgaroviedo_view(request):
    return render(request, 'main/edgaroviedo.html')


def github_projects(request):
    github_username = "TU_USUARIO"  # <-- Cambia esto
    url = f"https://api.github.com/users/{github_username}/repos"
    response = requests.get(url)
    
    if response.status_code == 200:
        repos = response.json()
    else:
        repos = []

    context = {
        "repos": repos
    }
    return render(request, "portfolio/github_projects.html", context)

@require_POST
@csrf_exempt  # Solo si no usas {% csrf_token %}. Si lo usas, puedes quitar esta línea.
def enviar_presupuesto(request):
    nombre = request.POST.get('nombre')
    correo = request.POST.get('correo')
    detalles = request.POST.get('detalles')

    mensaje = f"Nombre: {nombre}\nCorreo: {correo}\n\nDetalles:\n{detalles}"

    send_mail(
        subject="Nuevo presupuesto recibido",
        message=mensaje,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=['edgarkonectia@gmail.com'],  # CAMBIA esto a tu correo real
        fail_silently=False,
    )

    return JsonResponse({'success': True})