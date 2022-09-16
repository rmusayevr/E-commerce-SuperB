from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, CreateView
from .models import *
from .forms import ReviewForm
from django.db.models import Count, Q

class ProductListView(ListView):
    model = Product
    template_name = "product-list.html"
    paginate_by = 4
    context_object_name = "products"

    def get_queryset(self):
        category = self.request.GET.get("category")
        if category:
            return Product.objects.filter(category__name = category).order_by("-date").all()
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
        product = Product.objects.get(pk=self.kwargs.get("pk"))
        product.read_count += 1
        product.save()
        return product
        
    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context['images'] = Images_of_product.objects.filter(version__pk = self.kwargs.get("pk"))
        context['r_items'] = Product.objects.filter(Q(category = kwargs['object'].category), ~Q(pk = self.kwargs.get("pk"))).all()[:10]
        context['u_items'] = Product.objects.order_by("-review_count").filter(~Q(pk = self.kwargs.get("pk"))).all()[:5]
        context['reviews'] = Review.objects.filter(product__pk = self.kwargs.get("pk")).all()[:3]
        context['colors'] = Product_version.objects.filter(product__pk = self.kwargs.get("pk")).values_list('color', flat=True)
        return context
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = Product.objects.get(pk=self.kwargs.get("pk"))
            review.save()
            product = Product.objects.get(pk=self.kwargs.get("pk"))
            product.review_count += 1
            product.save()
        return redirect('product_detail', pk=self.kwargs.get("pk"))
