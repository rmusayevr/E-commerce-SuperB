from django.shortcuts import render, redirect,HttpResponse
from django.urls import reverse_lazy
from Product.models import Product
from django.db.models import Q
from .forms import AddressInfoForm, BillingInfoForm, ShippingInfoForm, OrderForm
from .models import Wishlist, basket, billing_addresses, shipping_addresses, order
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

class CheckoutView(LoginRequiredMixin, FormMixin, ListView):
    template_name = 'checkout.html'
    form_class = OrderForm
    model = billing_addresses
    context_object_name = 'addresses'

    def get_queryset(self):
        return billing_addresses.objects.filter(user_id = self.request.user).all()
        
    def get_context_data(self, **kwargs):
        context = super(CheckoutView, self).get_context_data(**kwargs)
        result = self.request.GET.get('result')
        if result == "COMPLETED":
            user_basket =  basket.objects.filter(user = self.request.user, is_active = True).first()
            for products in user_basket.product.all():
                products.quantity = 0
                products.save()
            user_basket.is_active = False
            user_basket.save()
        grand_total = 0
        products = Product.objects.filter(Q(products_basket__user__username = self.request.user.username), Q(products_basket__is_active = True)).all()
        for product in products:
            grand_total += product.get_subtotal()
        context['grand_total'] = grand_total
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            order_form = form.save(commit=False)
            order_form.user = self.request.user
            order_form.save()
        return redirect('index')

class BasketView(LoginRequiredMixin, ListView):
    model = basket
    template_name = 'shopping_cart.html'

    def get_context_data(self, **kwargs):
        context = super(BasketView, self).get_context_data(**kwargs)
        user_basket =  basket.objects.filter(Q(user = self.request.user), Q(is_active = True)).first()
        if user_basket:
            all_products = user_basket.product.all()
            context['baskets'] = all_products
        
        grand_total = 0
        products = Product.objects.filter(Q(products_basket__user__username = self.request.user.username), Q(products_basket__is_active = True)).all()
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

