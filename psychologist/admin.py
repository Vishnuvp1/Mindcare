from django.contrib import admin

from psychologist.models import Psychologist

# Register your models here.

class PsychologistAdmin(admin.ModelAdmin):
    list_display = ('profile_image','account','date_of_birth','gender', 'department', 
                  'experience','languages', 'skills',  'resume', 'certificate' , 'fees')

admin.site.register(Psychologist, PsychologistAdmin)