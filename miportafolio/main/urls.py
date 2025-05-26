from django.urls import path
from . import views
from .views import solicitar_presupuesto
from .views import edgaroviedo_view

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('presupuesto/', solicitar_presupuesto, name='presupuesto'),
    path('edgaroviedo/', edgaroviedo_view, name='edgaroviedo'),
    path("github/", views.github_projects, name="github_projects"),
    path('presupuesto/enviar/', views.enviar_presupuesto, name='enviar_presupuesto'),

]