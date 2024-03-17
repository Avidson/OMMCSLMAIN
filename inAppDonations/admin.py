from django.contrib import admin
from .models import *
# Register your models here.


class InAppDonationsAdmin(admin.ModelAdmin):

    list_display = [
        'client_name', 'amount', 'email', 'timestamp', 'paid', 'payment_purpose', 'payment_ref'  
    ]

admin.site.register(InAppDonations, InAppDonationsAdmin)