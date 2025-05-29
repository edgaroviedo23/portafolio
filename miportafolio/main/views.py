from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMessage
from .models import Comentario
from django.http import HttpResponse
from django.core import signing


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



def edgaroviedo_view(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        contenido = request.POST.get('contenido')

        if nombre and contenido:
            Comentario.objects.create(nombre=nombre, contenido=contenido)
            return redirect('edgaroviedo')  # Redirige para evitar reenvíos de formulario

    comentarios = Comentario.objects.order_by('-fecha')  # Más recientes primero

    return render(request, 'main/edgaroviedo.html', {'comentarios': comentarios})


# Cookies


def set_signed_cookie_view(request):
    response = HttpResponse("🔐 Cookie firmada establecida")
    response.set_signed_cookie('segura', 'dato123', salt='mi_salt', max_age=3600)
    return response

def get_signed_cookie_view(request):
    try:
        valor = request.get_signed_cookie('segura', salt='mi_salt')
        return HttpResponse(f"🔍 Cookie firmada: {valor}")
    except Exception:
        return HttpResponse("⚠️ Cookie inválida o manipulada")
    
def politica_cookies(request):
    return render(request, 'main/politica_cookies.html')