from django.contrib import admin
from .models import Twit



# Register your models here.

class TwitAdmin(admin.ModelAdmin):
	list_display = ('titulo','slug','fecha','publicado')
	list_filter  = ('publicado','fecha')
	search_fields = ('titulo','cuerpo')
	prepopulated_fields = {'slug':('titulo',)}


admin.site.register(Twit,TwitAdmin)#El registrer muestra en la vista de administrador