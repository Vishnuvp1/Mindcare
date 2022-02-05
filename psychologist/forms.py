from pyexpat import model
from django.forms import ModelForm
from accounts.models import Account

from psychologist.models import Psychologist, ConsultTime


class PsychologistForm(ModelForm):

    class Meta:
        model = Psychologist
        fields = ('profile_image', 'department', 'date_of_birth', 'gender',
                  'experience', 'languages', 'skills', 'resume', 'certificate', 'fees')

class ConsultForm(ModelForm):
    class Meta:
        model = ConsultTime
        fields = ('date', 'time')

