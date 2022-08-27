from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, CreateView
from .models import *
from .forms import ReviewForm


class ProductListView(ListView):
    model = Product_version
    template_name = "product-list.html"
    paginate_by = 4
    context_object_name = "products"

    def get_queryset(self):
        return Product_version.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.filter(is_navbar = "True").all()
        context['s_categories'] = Category.objects.filter(is_navbar = "False").all() 
        context['tags'] = Tags.objects.all()[:15]
        context['images'] = Images_of_product.objects.all()
        return context

class ProductDetailView(DetailView, CreateView):
    template_name = 'product-detail.html'
    pk_url_kwarg = 'pk'
    model = Product_version
    context_object_name = "product"
    form_class = ReviewForm

    def get_object(self, queryset=None):
        return Product_version.objects.get(pk=self.kwargs.get("pk"))
        
    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context['images'] = Images_of_product.objects.filter(version__pk = self.kwargs.get("pk"))
        context['image'] = Images_of_product.objects.filter(version__pk = self.kwargs.get("pk")).first()
        context['reviews'] = Review.objects.filter(version__pk = self.kwargs.get("pk")).all()[:3]
        return context
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.version = Product_version.objects.get(pk=self.kwargs.get("pk"))
            review.save()
        return redirect('product_detail', pk=self.kwargs.get("pk"))
