from django.contrib import admin
from main.models import *
from django.utils.safestring import mark_safe


def payment_pdf(obj):
    url = reverse('main:youmade-payment_pdf', args=[obj.pk])
    return mark_safe(f'<a href="{url}">PDF</a>') #This tells django template to allow this page to render
payment_pdf.short_description = 'Receipt'


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('profile_owner', 'first_name', 'last_name', 'occupation', 'state_residence', 
    'home_address', 'phone_number', 'registration_fee', 'paid', 'email', 'payment_date','payment_ref',
    'passport',
    payment_pdf
    )
admin.site.register(Profile, ProfileAdmin)


class MessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'message')
admin.site.register(Message, MessageAdmin)

#In line profile model


