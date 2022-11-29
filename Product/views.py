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
        parent_category = self.request.GET.get("parent_category")
        category = self.request.GET.get("category")
        if parent_category and not category:
            return Product_version.objects.filter(product__category__p_category__name = parent_category).order_by("-datetime").all()
        elif category:
            return Product_version.objects.filter(product__category__name = category, product__category__p_category__name = parent_category).order_by("-datetime").all() 
        return Product_version.objects.order_by("-datetime").all()

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.filter(is_navbar = "True").all()
        context['s_categories'] = Category.objects.filter(is_navbar = "False").all() 
        context['manufacturers'] = Manufacturer.objects.all()
        context['colors'] = Product_version.objects.values_list("color_id__name", flat=True).distinct().values('color_id__name').annotate(count = Count('color_id__name'))
        return context

class ProductDetailView(DetailView, CreateView):
    template_name = 'product-detail.html'
    pk_url_kwarg = 'pk'
    model = Product
    context_object_name = "product"
    form_class = ReviewForm

    def get_object(self, queryset=None):
        product = Product_version.objects.get(pk=self.kwargs.get("pk"))
        product.read_count += 1
        product.save()
        return product
        
    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context['images'] = Image.objects.all()
        context['r_items'] = Product_version.objects.filter(Q(product__category__p_category__name = kwargs['object'].product.category.p_category) | Q(product__category__name = kwargs['object'].product.category), ~Q(pk = self.kwargs.get("pk")), ~Q(product = kwargs["object"].product)).order_by('product').all().distinct('product')[:5]
        context['u_items'] = Product_version.objects.order_by("-review_count").filter(~Q(pk = self.kwargs.get("pk")), ~Q(product = kwargs["object"].product)).order_by('product').all().distinct('product')[:5]
        context['reviews'] = Review.objects.filter(product__pk = self.kwargs.get("pk")).all()[:3]
        context['colors'] = Product_version.objects.filter(product = kwargs["object"].product).all()
        return context
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = Product_version.objects.get(pk=self.kwargs.get("pk"))
            review.save()
            product = Product_version.objects.get(pk=self.kwargs.get("pk"))
            product.review_count += 1
            product.save()
        return redirect('product_detail', pk=self.kwargs.get("pk"))
