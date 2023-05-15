from django.contrib import admin
from .models import Producto
# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ["id","nombre","precio","descripcion","fecha_vencimiento"]
    list_editable = ["precio"]

admin.site.register(Producto,ProductoAdmin)