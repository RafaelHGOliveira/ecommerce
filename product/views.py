from django.http import Http404
from django.shortcuts import get_object_or_404, render

from .models import Product, Category
from django.core.paginator import Paginator


def index(request):

    products = Product.objects.all().order_by('-id')
    categories = Category.objects.all().order_by('-id')

    paginator = Paginator(products, 20)
    p = request.GET.get('page')
    products = paginator.get_page(p)

    return render(request, 'index.html', {
        'products': products,
        'categories': categories,
    })


def product_detail(request, product_id, slug):

    product = get_object_or_404(Product, id=product_id)

    categories = Category.objects.all().order_by('-id')

    if not product.active:
        raise Http404()
    return render(request, 'product_detail.html', {
        'product': product,
        'categories': categories,
    })
