from django.urls import reverse
from django.shortcuts import render, redirect
from orders.models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from .tasks import order_created

def order_create(request):
    
    cart  = Cart(request)

    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            order_id = (order.id)
            
            cart.clear()
            order_created.delay(order_id)
            return redirect(reverse('payment:process',args=[order_id,]),)


            # return render(request,'orders/order/created.html',
            #                                         {'order':order,})
    else:
        form = OrderCreateForm()

    return render(request,'orders/order/create.html',
                                            {'cart':cart,'form':form})