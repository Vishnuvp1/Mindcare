import json
from django.shortcuts import redirect, render
from urllib3 import HTTPResponse
from accounts.models import Account
from psychologist.models import ConsultTime, Psychologist
import json

from user.models import Appointment, Chat

# Create your views here.


def homepage(request):
    return render(request, 'user/home.html')


def service(request):
    return render(request, 'user/services.html')


def psychologists(request):
    psychologists = Psychologist.objects.all()
    context = {
        'psychologists': psychologists
    }
    return render(request, 'user/psychologist_list.html', context)


def psychologistdetails(request, id):
    try:
        print('iddd', id)
        request.session['id'] = id
        psycologist = Psychologist.objects.get(id=id)
        user = Account.objects.get(email=psycologist.account.email)
        psy = ConsultTime.objects.filter(account__id=user.id)
        print(psy)

    except Exception as e:
        print("Error")
        raise e

    context = {
        'psychologist': psycologist,
        'psy': psy
    }

    return render(request, 'user/psychologist_details.html', context)


def payment(request):
    id = request.session['id']
    psycologist = Psychologist.objects.get(id=id)
    context = {
        'psy': psycologist
    }
    return render(request, 'user/payment-page.html', context)


def paymentpaypal(request):
    return HTTPResponse('hii')


def paymentcompleted(request):
    return render(request, 'user/payment-completed.html')


def chatroom(request):
    id = request.session['id']
    if Account.objects.filter(id=id).exists():
        print("hi")

    return render(request, 'user/chatroom.html')


def appointment(request):
    user = request.user
    if request.method == 'POST':
        account = Account.objects.get(id=user.id)

        value = request.POST.get('radio')
        list = value.split(',')
        date = list[0]
        time = list[1]
        Appointment.objects.create(
            first_name=account.first_name, 
            last_name=account.last_name,
            email=account.email, 
            phone=account.phone, 
            date=date, time=time, 
            account=account
            )
        return redirect('payment')
    return render(request, 'user/chatroom.html')


def chat(request):
    pass
