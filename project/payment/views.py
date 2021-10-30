from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

import braintree
from orders.models import Order

def payment_process(request,order_id):

    order = get_object_or_404(Order, id=order_id)
    if request.method == "POST":
        # GET TOKEN .
        nonce = request.POST.get('payment_method_nonce', None)
        # Create and save transaction
        result = braintree.Transaction.sale({
            'amount': '{:.2f}'.format(order.get_total_cost()),
            'payment_method_nonce': nonce,
            'options': {
                'submit_for_settlement': True
            }
        })
        if result.is_success:
            # save as paid order
            order.paid = True
            #Save transaction id in order model.
            order.braintree_id = result.transaction.id
            order.save()
            return redirect('payment:done')
        else:
            return redirect('payment:canceled')
    else:
        try:
            client_token = braintree.ClientToken.generate()
        except:
            return redirect('payment:canceled',)
    return render(request, 'payment/process.html', {'order': order, 
                                    'client_token': client_token})


def payment_done(request):
    return render(request, 'payment/done.html')

def payment_canceled(request):
    return render(request, 'payment/canceled.html')
