from django.http import Http404
from django.shortcuts import get_object_or_404, render

from .models import Product, Category
from django.core.paginator import Paginator


def index(request):
    products = Product.objects.all().order_by('-id')
    categories = Category.objects.all().order_by('-id')

    # TODO: configure pagination
    paginator = Paginator(products, 50)
    p = request.GET.get('p')
    products = paginator.get_page(p)

    return render(request, 'index.html', {
        'products': products,
        'categories': categories,
    })


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if not product.active:
        raise Http404()
    return render(request, 'product_detail.html', {
        'product': product,
    })
