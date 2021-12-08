from django.http import JsonResponse
from django.core.mail import send_mail
import json
from django.core.mail import EmailMessage
from django.shortcuts import render


def index(request):
    return render(request, 'proamb/index.html')


def granos(request):
    return render(request, 'proamb/granos.html')


def industriahogar(request):
    return render(request, 'proamb/industriahogar.html')


def jardin(request):
    return render(request, 'proamb/jardin.html')


def maderes(request):
    return render(request, 'proamb/maderas.html')


def tanques(request):
    return render(request, 'proamb/tanques.html')


def send_json(request):
    data = {'result': True}

    mail_data = dict(request.GET)
    message = '''
Nombre: %s 
Email: %s
Telefono: %s        
%s
''' % (mail_data['name'][0],
       mail_data['email'][0],
       mail_data['phone'][0],
       mail_data['message'][0],
       )

    msj = EmailMessage(
        'Contacto web',
        message,
        'Contacto Website <odoo_sender@solvoweb.com>',
        ['marianoa.dangelo@gmail.com'],
        reply_to=mail_data['email'],
    )
    msj.send()

    return JsonResponse(data, safe=False)
