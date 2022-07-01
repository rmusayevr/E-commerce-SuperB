from django.shortcuts import render

def product_detail(request):
    return render(request, "product_detail.html")

def product_list(request):
    return render(request, "product_list.html")

def quick_view(request):
    return render(request, "quick_view.html")
