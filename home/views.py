from django.shortcuts import render
from .models import Client, Info, Service
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.
def home(request):
    info = Info.objects.first()
    service = Service.objects.all()
    context= {'info': info, 'service': service}
    return render(request, 'home/index.html', context)



class ContactCreate(CreateView, SuccessMessageMixin):
    model = Client
    fields = ["name", "email", "phone", 'message']
    success_url = reverse_lazy("home")
    success_message = 'لقد تم ارسال رسالتك وسوف يتم الاتصال بيك في أقرب وقت'