from django.contrib import admin

# Register your models here.
from .models import Categoria, Producto, Cliente

def aumentar_stock(modeladmin, request, queryset):
    incremento = 20

    for producto in queryset:
        producto.stock += incremento
        producto.save()
    
    modeladmin.message_user(request, f"Stock incrementado en {incremento} unidades para los productos seleccionados.")

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'categoria', 'stock')
    search_fields = ('nombre', 'categoria__nombre')
    actions = [aumentar_stock]

admin.site.register(Categoria)
admin.site.register(Cliente)