from django.shortcuts import redirect, render
from django.views import View
from django.contrib import messages, auth
from accounts.models import Account
from psychologist.models import Psychologist
from . forms import PsychologistForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login


# Create your views here.


def register(request):
    if request.method == 'POST':
        form = PsychologistForm(request.POST, request.FILES)
        if form.is_valid():
            data = Psychologist()
            data.first_name = form.cleaned_data['first_name']
            data.last_name = form.cleaned_data['last_name']
            data.username = form.cleaned_data['username']
            data.email = form.cleaned_data['email']
            data.phone = form.cleaned_data['phone']
            data.gender = form.cleaned_data['gender']
            data.date_of_birth = form.cleaned_data['date_of_birth']
            data.address = form.cleaned_data['address']
            data.experience = form.cleaned_data['experience']
            data.resume = form.cleaned_data['resume']
            data.certificate = form.cleaned_data['certificate']
            data.password = form.cleaned_data['password']
            psychologist = Account.objects.create_psychologist(
                first_name=data.first_name, last_name=data.last_name, phone=data.phone, username=data.username,
                email=data.email, password=data.password)
            data.save()
            psychologist.save()
            auth.login(request, psychologist)
            messages.success(request, "Registered")
            return redirect('psychologist_signin')
    else:
        form = PsychologistForm(request.POST, request.FILES)
    context = {'form': form}
    return render(request, 'psychologist/register.html', context)


def signin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        psychologist = auth.authenticate(email=email, password=password)
        if psychologist is not None:
            if psychologist.is_staff:
                auth.login(request, psychologist)
                return redirect('psychologist_home')
            else:
                print('blocked')
        else:
            pass
    else:
        return render(request, 'psychologist/signin.html')


@login_required(login_url='psychologist_signin')
def homepage(request):
    return render(request, 'psychologist/home.html')


def signout(request):
    auth.logout(request)
    return redirect('psychologist_signin')
