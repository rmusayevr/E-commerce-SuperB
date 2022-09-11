from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from Product.models import Product
from .forms import AddressInfoForm, BillingInfoForm, ShippingInfoForm, GetQuantityForm
from .models import Wishlist, basket, billing_addresses, shipping_addresses
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView
from django.views.generic.edit import FormMixin


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

class BasketView(LoginRequiredMixin, FormMixin, ListView):
    model = basket
    template_name = 'shopping_cart.html'
    form_class = GetQuantityForm

    
        
    def get_context_data(self, **kwargs):
        context = super(BasketView, self).get_context_data(**kwargs)
        user_basket =  basket.objects.filter(user = self.request.user).first()
        if user_basket:
            all_products = user_basket.product.all()
            context['baskets'] = all_products
        
        grand_total = 0
        products = Product.objects.filter(products_basket__user__username = self.request.user.username).all()
        for product in products:
            grand_total += product.get_subtotal()
        context['grand_total'] = grand_total
        return context
    
class WishlistView(LoginRequiredMixin, ListView):
    model = Wishlist
    template_name = 'wishlist.html'

    def get_context_data(self, **kwargs):
        context = super(WishlistView, self).get_context_data(**kwargs)
        user_wishlist =  Wishlist.objects.filter(user = self.request.user).first()
        if user_wishlist:
            all_products = user_wishlist.product_ver.all()
            context['items'] = all_products
        return context