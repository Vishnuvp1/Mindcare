from django.contrib import admin

from psychologist.models import Psychologist

# Register your models here.

class PsychologistAdmin(admin.ModelAdmin):
    list_display = ()

admin.site.register(Psychologist)