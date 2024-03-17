from io import BytesIO
from celery import shared_task
import weasyprint
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
from main.models import *

@shared_task
def payment_completed(order_id):
    """
    Task to send an e-mail notification when an order is
    successfully created.
    """
    your_invoice = 'your invoice'
    payment = Profile.objects.get(pk=order_id)
    # create invoice e-mail
    subject = f'OMMCSL - Invoice no. {payment.pk}'
    message = '''Please, find attached the invoice for your recent payment for OMMCSL membership
     filling on our database.'''
     
    email = EmailMessage(subject,
                         message,
                         'info@ommcsl.loan',
                         [payment.email])
    # generate PDF
    html = render_to_string('main/pdf.html', {'payment': payment})
    out = BytesIO()
    stylesheets=[weasyprint.CSS(settings.STATIC_ROOT + 'assets/css/passcode.css')]
    weasyprint.HTML(string=html).write_pdf(out, stylesheets=stylesheets)
    # attach PDF file
    email.attach(f'{your_invoice}-{payment.payment_date}-{payment.pk}.pdf',
                 out.getvalue(),
                 'application/pdf')
    # send e-mail
    email.send()