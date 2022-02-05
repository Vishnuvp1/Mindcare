from django.contrib import admin

from psychologist.models import Psychologist, ConsultTime

# Register your models here.

class PsychologistAdmin(admin.ModelAdmin):
    list_display = ('profile_image','account','date_of_birth','gender', 'department', 
                  'experience','languages', 'skills',  'resume', 'certificate' , 'fees')

class ConsultTimeAdmin(admin.ModelAdmin):
    list_display = ('account', 'date', 'time')

admin.site.register(Psychologist, PsychologistAdmin)
admin.site.register(ConsultTime, ConsultTimeAdmin)