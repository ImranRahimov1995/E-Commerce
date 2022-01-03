from django.core.mail import send_mail
from .models import Order
from config.celery import app


@app.task
def order_created(order_id):
    """Задача отправки email-уведомлений при успешном оформлении заказа."""
    order = Order.objects.get(id=order_id)
    subject = 'Order nr. {}'.format(order.id)
    message = 'Dear {},\n\nYou have successfully placed an order.\
                    Your order id is {}.'.format(order.first_name,
                                                 order.id)
    mail_sent = send_mail(subject,
                          message,recipient_list=[order.email])
    return mail_sent
