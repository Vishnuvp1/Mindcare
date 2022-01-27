from django.forms import ModelForm
from accounts.models import Account

from psychologist.models import Psychologist


class PsychologistForm(ModelForm):

    class Meta:
        model = Psychologist
        fields = ('address', 'date_of_birth', 'gender',
                  'experience', 'resume', 'certificate')
