from django.shortcuts import redirect, render
from accounts.forms import RegistrationForm
from accounts.models import Account
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages, auth
from accounts.verification import send_otp, verify_otp_number

# Create your views here.


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
            user = Account.objects.create_user(
                first_name=first_name, last_name=last_name, email=email, username=username, password=password, phone=phone)

            request.session['phone'] = phone
            send_otp(phone)

            # user.save()
            messages.info(request, 'Enter your OTP number.')
            return redirect('otp_verify')

    else:
        form = RegistrationForm()
    context = {
        'form': form
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


@login_required(login_url='signin')
def signout(request):
    auth.logout(request)
    messages.success(request, 'You are logged out.')
    return redirect('homepage')


def otp_page(request):
    return render(request, 'otp.html')


def otp_verify(request):
    if request.user.is_authenticated:
        return redirect('homepage')

    if request.method == 'POST':
        try:
            phone = request.session['phone']
        except KeyError:
            messages.info(request, 'Session timeout')
            return redirect('signin')

        otp = request.POST.get('otp')
        print(otp)
        verified = verify_otp_number(phone, otp)
        print('verified')

        if verified:
            user = Account.objects.get(phone=phone)
            user.is_verified = True
            user.save()
            auth.login(request, user)
            messages.success(request, 'Successfully account verified')
            return redirect('homepage')
        else:
            messages.error(request, 'Invalid OTP, please try again')
            return redirect('otp_verify')

    return render(request, 'user/otp_page.html')
