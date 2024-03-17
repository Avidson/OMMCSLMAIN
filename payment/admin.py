from django.contrib import admin

from . models import *
# Register your models here.


class Paymentdmin(admin.ModelAdmin):
    list_display = ('id','first_name', 'last_name', 'email', 'amount', 
                    'created', 'updated', 'paid', 'paystack_ref', 'payment_purpose'
                    )
    list_filter = [
            'paid', 'created', 'updated'
    ]
admin.site.register(Payment, Paymentdmin)
