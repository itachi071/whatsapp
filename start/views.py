from django.shortcuts import redirect, render
from .models import *
from twilio.rest import Client
from django.conf import settings


def home(request):
    return render(request,'index.html')

def send_message(request):
    if request.method =='POST':
        name=request.POST.get('name')
        file=request.FILES.get('file')
        form=Upload_Data(Name=name,File=file)
        form.save()
        client = Client(settings.TWILIO_ACCOUNT_SID,settings.TWILIO_AUTH_TOKEN)
        print(settings.TWILIO_ACCOUNT_SID)
        media_message = client.messages.create(
        from_=f'whatsapp:+14155238886',
        to=f'whatsapp:{settings.CLIENT_PHONE_NUMBER}',
        body=f'hello {name}') 
        return redirect('/')
    return render(request,'index.html')