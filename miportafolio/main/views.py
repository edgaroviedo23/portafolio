from django.shortcuts import render
from django.core.mail import send_mail
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

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


@require_POST
@csrf_exempt  # Quita esta línea si usas csrf_token en tu formulario
def enviar_presupuesto(request):
    nombre = request.POST.get('nombre')
    correo = request.POST.get('correo')
    detalles = request.POST.get('detalles')

    mensaje = f"Nombre: {nombre}\nCorreo: {correo}\n\nDetalles:\n{detalles}"

    send_mail(
        subject="Nuevo presupuesto recibido",
        message=mensaje,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=['edgarkonectia@gmail.com'],  # Cambia a tu correo real
        fail_silently=False,
    )

    return JsonResponse({'success': True})

