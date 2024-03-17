
from celery import task
from django.core.mail import send_mail

from payment.models import Payment

@task
def payment_created(payment_id):
    """
    Task to send an e-mail notification when an payment is
    successfully created.
    """
    payment = Payment.objects.get(id=payment_id)
    subject = f'Paymment with ref: {payment.id}'
    message = f'Dear {payment.first_name},\n\n' \
              f"""You have successfully made a payment on OMMCSL 
               Multipurpose Cooperative. 
               The payment was made in respect to {payment.payment_purpose}""" \
              f'Your payment ID is {payment.id}. \n\n' \
              f'Amount paid was the sum of {payment.amount}'
                

    mail_sent = send_mail(subject,
                          message,
                          'admin@myshop.com',
                          [payment.email])
    return mail_sent