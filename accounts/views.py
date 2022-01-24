from django.shortcuts import redirect, render
from accounts.forms import RegistrationForm
from accounts.models import Account
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages, auth

# Create your views here.

# @login_required(login_url='signin')
def homepage(request):
    return render(request, 'user/home.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            username = email.split("@")[0]
            user = Account.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password ,phone=phone)

            print(phone)
            
            user.save()
            return redirect('signin')
            
    else:
        form = RegistrationForm()
    context = {
        'form' : form
    }
    return render(request, 'user/register.html', context)


def signin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request.POST, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('homepage') 

    return render(request, 'user/signin.html')


@login_required(login_url = 'signin')
def signout(request):
    auth.logout(request)
    messages.success(request, 'You are logged out.')
    return redirect('homepage')