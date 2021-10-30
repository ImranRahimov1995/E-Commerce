from config.celery import app
from orders.models import Order

from  django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings

import weasyprint
from io import BytesIO


@app.task
def send_order_pdf(order_id):
    order = Order.objects.get(pk=order_id)
    subject = 'My Shop - Invoice no. {}'.format(order.id)
    message = 'Please, find attached the invoice for your recent purchase.'
    email = EmailMessage(subject,
                            message,
                            'admin@myshop.com',
                            [order.email])
    # generate PDF
    html = render_to_string('orders/order/pdf.html', {'order': order})
    out = BytesIO()
    stylesheets=[weasyprint.CSS(settings.STATIC_ROOT / 'css/pdf.css')]
    weasyprint.HTML(string=html).write_pdf(out,
                                            stylesheets=stylesheets)
    # attach PDF file
    email.attach('order_{}.pdf'.format(order.id),
                    out.getvalue(),
                    'application/pdf')
    email.send()