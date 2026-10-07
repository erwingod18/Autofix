from django.contrib import admin

from .models import especialidad, OrdenReparacion
# Register your models here.

class OrdenReparacionInline(admin.TabularInline):
    model = OrdenReparacion
    extra = 1

@admin.register(especialidad)
class EspecialidadAdmin(admin.ModelAdmin):
    inlines = [OrdenReparacionInline]
    list_display = ("nombre", "total_ordenes")

    @admin.display(description="Total de órdenes")
    def total_ordenes(self, obj):
        return obj.ordenes_reparacion.count()


@admin.register(OrdenReparacion)
class OrdenReparacionAdmin(admin.ModelAdmin):
    actions = ["marcar_como_listo"]
    list_display = (
        "codigo_orden",
        "patente_vehiculo",
        "modelo_vehiculo",
        "cliente_nombre",
        "costo_estimado",
        "estado",
        "fecha_ingreso",
        "especialidad",
    )
    list_filter = ["estado", "especialidad", "fecha_ingreso"]
    list_editable = ["estado"]
    search_fields = ["codigo_orden"]

    @admin.action(description="Marcar órdenes seleccionadas como listas")
    def marcar_como_listo(self, request, queryset):
        total = queryset.update(estado="LISTO")
        self.message_user(request, f"{total} órdenes marcadas como listas.")