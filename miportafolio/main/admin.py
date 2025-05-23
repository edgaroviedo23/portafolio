from django.contrib import admin
from .models import Proyecto, Comentario, Presupuesto

admin.site.register(Proyecto)
admin.site.register(Comentario)
admin.site.register(Presupuesto)

