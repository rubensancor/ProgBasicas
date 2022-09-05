from django.contrib import admin

from .models import *

class ContenidoRamaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'rama')

admin.site.register(Er)
admin.site.register(Trimestre)
admin.site.register(Monte)
admin.site.register(Rama)
admin.site.register(Campamento)
admin.site.register(Taller)
admin.site.register(Reunion)
admin.site.register(Simbolo)
admin.site.register(Paso)
admin.site.register(ContenidoRama, ContenidoRamaAdmin)
admin.site.register(ContenidoTrimestre)
admin.site.register(ContenidoCampa)
admin.site.register(Recurso)

