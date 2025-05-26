from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

from .forms import PresupuestoForm

def presupuesto(request):
    if request.method == 'POST':
        form = PresupuestoForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            email = form.cleaned_data['email']
            mensaje = form.cleaned_data['mensaje']

            try:
                send_mail(
                    subject='Solicitud de presupuesto',
                    message=f"Nombre: {nombre}\nEmail: {email}\nMensaje: {mensaje}",
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=['edgarkonectia@gmail.com'],
                    fail_silently=False,
                )
                return render(request, 'main/gracias.html')

            except Exception as e:
                logger.error("Error enviando correo:", exc_info=e)
                form.add_error(None, "Error enviando el correo. Intenta más tarde.")

    else:
        form = PresupuestoForm()

    return render(request, 'main/presupuesto.html', {'form': form})
