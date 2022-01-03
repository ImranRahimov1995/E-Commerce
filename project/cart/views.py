
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Product
from cart.cart import Cart
from cart.forms import CartAddProductForm
from coupons.forms import CouponApplyForm
from shop.recommender import Recommender

@require_POST
def cart_add(request, product_id):

    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)

    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'],
                             update_quantity=cd['update'])

    return redirect('cart:cart_detail')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    if len(cart) == 0:
        print(len(cart),'is zero')
        return redirect('shop:product_list')
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    r = Recommender()

    #Change quantity in cart
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={
                        "quantity": item['quantity'], 
                        'update': True, })
    coupon_apply_form = CouponApplyForm()

    cart_products = [item['product'] for item in cart]
    recommended_products = r.suggest_products_for(cart_products)

    return render(request, 'cart/detail.html',
                {'coupon_apply_form':coupon_apply_form,
                'recommended_products':recommended_products })