from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def index(request):
    send_mail('Sent from django', 'SWD TEST', 'kawin.phonklam@gmail.com', ['TO EMAIL'], fail_silently=False)