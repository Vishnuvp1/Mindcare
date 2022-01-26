from django.forms import ModelForm

from psychologist.models import Psychologist


class PsychologistForm(ModelForm):

    class Meta:
        model = Psychologist
        fields = ('first_name', 'last_name', 'username', 'email', 'phone', 'gender',
                  'date_of_birth', 'address', 'experience', 'resume', 'certificate', 'password')

