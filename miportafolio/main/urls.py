from django.urls import path
from . import views
from .views import edgaroviedo_view
from .views import enviar_presupuesto

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('edgaroviedo/', edgaroviedo_view, name='edgaroviedo'),
    path('presupuesto/', enviar_presupuesto, name='presupuesto'),  # ✅ Esta es la correcta
]