from django.http import Http404
from django.shortcuts import get_object_or_404, render

from .models import Product, Category
from django.core.paginator import Paginator


def index(request):
    products = Product.objects.all()
    
    # TODO: configure pagination
    # paginator = Paginator(products, 20)
    # p = request.GET.get('p')
    # products = paginator.get(p)
    
    return render(request, 'index.html', {
        'products': products,
    })


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if not product.mostrar:
        raise Http404()
    return render(request, 'product_detail.html', {
        'product': product,
    })
    