from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm


def product_list(request, category_slug=None):
    """ Get all available products"""

    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    context = {
        'categories': categories,
        'category': category,
        'products': products,
    }

    return render(request, 'shop/product/list.html', context)


def product_detail(request, id, slug):
    """ Get concrete available product by id"""

    product = get_object_or_404(Product, id=id, slug=slug,
                                 available=True)
    cart_product_form = CartAddProductForm()


    return render(request, 'shop/product/detail.html',{
                            'product': product,
                            'cart_product_form':cart_product_form,})