from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMessage

def inicio(request):
    return render(request, 'main/inicio.html')

def edgaroviedo_view(request):
    return render(request, 'main/edgaroviedo.html')


def enviar_presupuesto(request):
    mensaje_enviado = False
    error_envio = False

    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        correo = request.POST.get('correo')
        detalles = request.POST.get('detalles')

        asunto = f"Solicitud de presupuesto de {nombre}"
        cuerpo = f"Correo: {correo}\n\nDetalles del proyecto:\n{detalles}"

        try:
            email = EmailMessage(
                subject=asunto,
                body=cuerpo,
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[settings.DEFAULT_FROM_EMAIL],
                reply_to=[correo],  # para que al responder te conteste el usuario
            )
            email.content_subtype = "plain"  # para que sea texto plano
            email.encoding = 'utf-8'  # aquí indicas la codificación correcta
            email.send(fail_silently=False)
            mensaje_enviado = True
            print("Correo enviado con éxito")
        except Exception as e:
            error_envio = True
            print(f"Error enviando correo: {e}")

    return render(request, 'main/presupuesto.html', {
        'mensaje_enviado': mensaje_enviado,
        'error_envio': error_envio
    })
