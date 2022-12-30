from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import CreateView, ListView
from .models import FAQ
from django.db.models import Q
from Blog.models import Blog
from Product.models import Product_version
from .forms import ContactUsForm

class HomePage(ListView):
    template_name = 'index.html'
    model = Blog
    context_object_name = 'blogs'

    def get_queryset(self):
        return Blog.objects.order_by("-date").all()[:2]

    def get_context_data(self, **kwargs):
        context = super(HomePage, self).get_context_data(**kwargs)
        context['items'] = Product_version.objects.order_by("-datetime").all()[:10]
        context['featured_items'] = Product_version.objects.order_by("-read_count").all()[:4]
        context['best_items'] = Product_version.objects.order_by("-review_count").all()[:4]
        context['new_items'] = Product_version.objects.order_by("-datetime").all()[:4]
        return context

class ContactUs(CreateView):
    template_name = 'contact_us.html'
    form_class = ContactUsForm

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Your comment has been sent successfully!')
        return redirect('contact_us')

class FAQ(ListView):
    template_name = 'faq.html'
    model = FAQ
    context_object_name = 'faqs'

class Search(ListView):
    model = Product_version
    template_name = 'search.html'
    context_object_name = 'products'

    def get_queryset(self):
        query = self.request.GET.get('search')
        products=Product_version.objects.filter(Q(product__name__icontains=query))[:6]
        return products

def error(request):
    return render(request, "404error.html")
    
def about_us(request):
    return render(request, "about_us.html")