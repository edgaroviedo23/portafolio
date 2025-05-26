from django.shortcuts import render
from django.core.mail import send_mail
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

from .forms import PresupuestoForm


def inicio(request):
    return render(request, 'main/inicio.html')


def solicitar_presupuesto(request):
    return render(request, 'main/presupuesto.html', {'form': PresupuestoForm()})

def edgaroviedo_view(request):
    # tu lógica aquí
    return render(request, 'main/edgaroviedo.html') 

def github_projects(request):
    # Puedes personalizar esto
    return render(request, 'main/github_projects.html')


def presupuesto(request):
    if request.method == 'POST':
        form = PresupuestoForm(request.POST)
        if form.is_valid():
            send_mail(
                'Solicitud de presupuesto',
                f"Nombre: {form.cleaned_data['nombre']}\nEmail: {form.cleaned_data['email']}\nMensaje: {form.cleaned_data['mensaje']}",
                settings.DEFAULT_FROM_EMAIL,  # Remitente (tu email)
                ['edgarkonectia@gmail.com'],  # Destinatario (tu correo real)
                fail_silently=False,
            )
            return render(request, 'main/gracias.html')
    else:
        form = PresupuestoForm()
    return render(request, 'main/presupuesto.html', {'form': form})


@csrf_exempt  # Quita si usas {% csrf_token %}
def enviar_presupuesto(request):
    if request.method != "POST":
        return JsonResponse({'success': False, 'error': 'Método no permitido'}, status=405)

    nombre = request.POST.get('nombre')
    correo = request.POST.get('correo')
    detalles = request.POST.get('detalles')

    mensaje = f"Nombre: {nombre}\nCorreo: {correo}\n\nDetalles:\n{detalles}"

    try:
        send_mail(
            subject="Nuevo presupuesto recibido",
            message=mensaje,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=['edgarkonectia@gmail.com'],
            fail_silently=False,
        )
        return JsonResponse({'success': True})
    
    except Exception as e:
        logger.error("Error al enviar el correo:", exc_info=e)
        print("❌ ERROR AL ENVIAR CORREO:", e)  # <-- Esto aparecerá en Railway
        return JsonResponse({'success': False, 'error': str(e)}, status=500)
