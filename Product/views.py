from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, CreateView
from .models import *
from .forms import ReviewForm
from django.db.models import Count

class ProductListView(ListView):
    model = Product
    template_name = "product-list.html"
    paginate_by = 4
    context_object_name = "products"

    def get_queryset(self):
        return Product.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.filter(is_navbar = "True").all()
        context['s_categories'] = Category.objects.filter(is_navbar = "False").all() 
        context['manufacturers'] = Product.objects.values_list("manufacturer", flat=True).distinct().values('manufacturer')
        context['colors'] = Product_version.objects.values_list("color", flat=True).distinct().values('color').annotate(count = Count('color'))
        return context

class ProductDetailView(DetailView, CreateView):
    template_name = 'product-detail.html'
    pk_url_kwarg = 'pk'
    model = Product
    context_object_name = "product"
    form_class = ReviewForm

    def get_object(self, queryset=None):
        return Product.objects.get(pk=self.kwargs.get("pk"))
        
    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context['images'] = Images_of_product.objects.filter(version__pk = self.kwargs.get("pk"))
        context['image'] = Images_of_product.objects.filter(version__pk = self.kwargs.get("pk")).first()
        context['reviews'] = Review.objects.filter(product__pk = self.kwargs.get("pk")).all()[:3]
        return context
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = Product.objects.get(pk=self.kwargs.get("pk"))
            review.save()
            product = ProductStatistic.objects.get(product = self.get_object())
            product.reviews += 1
            product.save()
        return redirect('product_detail', pk=self.kwargs.get("pk"))
