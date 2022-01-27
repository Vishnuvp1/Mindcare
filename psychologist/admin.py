from django.contrib import admin

from psychologist.models import Psychologist

# Register your models here.

class PsychologistAdmin(admin.ModelAdmin):
    list_display = ('psychologist','date_of_birth', 'address', 'gender',
                  'experience', 'resume', 'certificate')

admin.site.register(Psychologist, PsychologistAdmin)