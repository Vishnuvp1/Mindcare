from django.shortcuts import render
from psychologist.models import Psychologist

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
        request.session['id'] = id
        psycologist = Psychologist.objects.get(id=id)
    except Exception as e:
        raise e

    context = {
        'psychologist': psycologist
    }
    return render(request, 'user/psychologist_details.html', context)


def payment(request):
    id = request.session['id']
    psycologist = Psychologist.objects.get(id=id)
    context = {
        'psy': psycologist
    }
    return render(request, 'user/payment.html', context)
