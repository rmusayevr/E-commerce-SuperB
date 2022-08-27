from operator import add
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from .forms import AddressInfoForm, BillingInfoForm, ShippingInfoForm
from .models import billing_addresses, shipping_addresses
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from django.contrib.auth import get_user_model
from User.models import User


class BillingInfo(LoginRequiredMixin, CreateView):
    form_class = BillingInfoForm
    success_url = reverse_lazy('index')
    template_name = 'billing_info.html'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            billing = form.save(commit=False)
            billing.user_id = self.request.user
            billing.save()
        return redirect('index')

class ShippingInfo(LoginRequiredMixin, CreateView):
    form_class = ShippingInfoForm
    success_url = reverse_lazy('index')
    template_name = 'shipping_info.html'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            shipping = form.save(commit=False)
            shipping.user_id = self.request.user
            shipping.save()
        return redirect('index')

class AddressInfo(LoginRequiredMixin, CreateView):
    form_class = AddressInfoForm
    success_url = reverse_lazy('index')
    template_name = 'address_info.html'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.user_id = self.request.user
            address.save()
            if address.is_billing == True:
                billing = billing_addresses(
                    first_name = form.cleaned_data.get('first_name'),
                    last_name = form.cleaned_data.get('last_name'),
                    telephone = form.cleaned_data.get('telephone'),
                    email = form.cleaned_data.get('email'),
                    street_address = form.cleaned_data.get('street_address'),
                    country = form.cleaned_data.get('country'),
                    city = form.cleaned_data.get('city'),
                    province = form.cleaned_data.get('province'),
                    zip = form.cleaned_data.get('zip'),
                    user_id = self.request.user
                )
                billing.save()
            if address.is_shipping == True:
                shipping = shipping_addresses(
                    first_name = form.cleaned_data.get('first_name'),
                    last_name = form.cleaned_data.get('last_name'),
                    telephone = form.cleaned_data.get('telephone'),
                    email = form.cleaned_data.get('email'),
                    street_address = form.cleaned_data.get('street_address'),
                    country = form.cleaned_data.get('country'),
                    city = form.cleaned_data.get('city'),
                    province = form.cleaned_data.get('province'),
                    zip = form.cleaned_data.get('zip'),
                    user_id = self.request.user
                )
                shipping.save()
        return redirect('index')

@login_required
def checkout(request):
    return render(request, "checkout.html")

@login_required
def shopping_cart(request):
    return render(request, "shopping_cart.html")

@login_required
def wishlist(request):
    return render(request, "wishlist.html")

