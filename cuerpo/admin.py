from django.contrib import admin
from .models import User, Cita, Opiniones, Producto

# Register your models here.

admin.site.register(User)
admin.site.register(Cita)
admin.site.register(Opiniones)
admin.site.register(Producto)
