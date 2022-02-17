from django.shortcuts import redirect, render
from accounts.models import Account
from psychologist.models import Psychologist
from django.contrib.auth.decorators import login_required
from django.contrib import messages, auth


def adminsignin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email, password=password)

        if user is not None:
            if user.is_admin:
                auth.login(request, user)

                return redirect('adminpanel')
            else:
                messages.error(request, 'You are not admin!')
                return redirect('adminsignin')
        else:
            messages.error(request, 'Invalid login credentials!')
            return redirect('adminsignin')

    return render(request, 'adminpanel/signin.html')


def adminsignout(request):
    auth.logout(request)
    messages.success(request, 'You are Logged out.')
    return redirect('adminsignin')


@login_required(login_url='adminsignin')
def adminpanel(request):
    return render(request, 'adminpanel/home.html')


def adminlogin(request):
    return render(request, 'adminpanel/adminlogin.html')


def userlist(request):
    users = Account.objects.all().filter(is_staff=False).order_by('id')

    context = {
        'users': users,
    }
    return render(request, 'adminpanel/user-list.html', context)


def psychologistlist(request):
    users = Psychologist.objects.all().filter(account__is_verified=True).order_by(
        'account__id').exclude(account__is_superadmin=True)

    context = {
        'users': users,
    }
    return render(request, 'adminpanel/psychologist-list.html', context)


def guestpsychologist(request):
    users = Psychologist.objects.all().filter(account__is_staff=True).order_by(
        '-account__id').exclude(account__is_superadmin=True)

    context = {
        'users': users,
    }
    return render(request, 'adminpanel/guestpsychologist.html', context)

def verifypsychologist(request, id):
    user = Account.objects.get(id=id)
    user.is_verified = True
    user.save()
    return redirect('guestpsychologist')
