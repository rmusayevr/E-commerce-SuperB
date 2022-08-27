from django.shortcuts import render, redirect
from .models import FAQ
from .forms import ContactUsForm, SubscriptionForm

def error(request):
    return render(request, "404error.html")
    
def about_us(request):
    return render(request, "about_us.html")

def contact_us(request):
    if request.method == "POST":
        contact_us_form = ContactUsForm(request.POST)
        if contact_us_form.is_valid():
            contact_us_form.save()
            return redirect('contact_us')
    else: 
        contact_us_form = ContactUsForm()
    context = {
        "form": contact_us_form
    }
    return render(request, "contact_us.html", context)

def faq(request):
    faqs = FAQ.objects.all()
    context = {
        "faqs": faqs
    }
    return render(request, "faq.html", context)

def index(request):
    if request.method == "POST":
        sub_form = SubscriptionForm(request.POST)
        if sub_form.is_valid():
            sub_form.save()
            return redirect('index')
    else: 
        sub_form = SubscriptionForm()
    context = {
        "form": sub_form
    }
    return render(request, "index.html", context)