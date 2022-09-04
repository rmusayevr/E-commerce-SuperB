from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView
from .models import FAQ
from .forms import ContactUsForm

def error(request):
    return render(request, "404error.html")
    
def about_us(request):
    return render(request, "about_us.html")

class ContactUs(CreateView):
    template_name = 'contact_us.html'
    form_class = ContactUsForm

class FAQ(ListView):
    template_name = 'faq.html'
    model = FAQ
    context_object_name = 'faqs'

def index(request):
    return render(request, "index.html")