from multiprocessing import context
from django.shortcuts import redirect, render
from django.views import View
from django.contrib import messages, auth
from accounts.forms import RegistrationForm
from accounts.models import Account
from psychologist.models import Psychologist, ConsultTime
from . forms import ConsultForm, PsychologistForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login


# Create your views here.


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            password = form.cleaned_data['password']
            user = Account.objects.create_psychologist(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone=phone,
                password=password)
            auth.login(request, user)
            messages.success(request, "Registered")
            return redirect('psychologist_signin')
    else:
        form = RegistrationForm(request.POST)
    context = {
        'form': form,
    }
    return render(request, 'psychologist/register.html', context)


def signin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email, password=password)
        if user:
            auth.login(request, user)
            if user is not None:
                if user.is_verified:
                    print('mail....')
                    return redirect('psychologist_home')
                elif user.is_staff:
                    print('staff')
                    return redirect('psychologist_verify')
                else:
                    return redirect('psychologist_profile')
        else:
            messages.error(request, 'Document deleted.')
            print('Not authenticated!!!!')

    return render(request, 'psychologist/signin.html')


@login_required(login_url='psychologist_signin')
def homepage(request):
    return render(request, 'psychologist/home.html')


def signout(request):
    auth.logout(request)
    return redirect('psychologist_signin')


@login_required(login_url='psychologist_signin')
def profile(request):
    # print(request.user)
    if request.method == 'POST':
        user = request.user
        form = PsychologistForm(request.POST, request.FILES)
        if form.is_valid():
            profile_image = form.cleaned_data['profile_image']
            gender = form.cleaned_data['gender']
            date_of_birth = form.cleaned_data['date_of_birth']
            fees = form.cleaned_data['fees']
            department = form.cleaned_data['department']
            experience = form.cleaned_data['experience']
            languages = form.cleaned_data['languages']
            skills = form.cleaned_data['skills']
            resume = form.cleaned_data['resume']
            certificate = form.cleaned_data['certificate']
            psy = Psychologist()
            psy.account = user
            psy.profile_image = profile_image
            psy.gender = gender
            psy.date_of_birth = date_of_birth
            psy.fees = fees
            psy.department = department
            psy.experience = experience
            psy.languages = languages
            psy.skills = skills
            psy.resume = resume
            psy.certificate = certificate
            psy.save()
            if not user.is_staff:
                user.is_staff = True
                user.save()

            messages.success(request, "Signin")
            return redirect('psychologist_verify')
    else:
        form = PsychologistForm(request.POST, request.FILES)
    context = {
        'form': form,
    }
    return render(request, 'psychologist/profile.html', context)


def verify(request):
    return render(request, 'psychologist/psychologist_verify.html')


def availability(request):
    print(request.user)
    if request.method == 'POST':
        user = request.user
        form = ConsultForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data['date']
            time = form.cleaned_data['time']
            consult = ConsultTime()
            consult.account = user
            consult.date = date
            consult.time = time
            consult.save()
            messages.success(request, "Successfully added date and time")
            return redirect('psychologist_availability')
    else:
        form = ConsultForm(request.POST)
    context = {
        'form': form,
    }
    return render(request, 'psychologist/psychologist_availability.html', context)
