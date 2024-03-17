from django.contrib import admin
from . models import *
# Register your models here.
from django.contrib.auth.models import *



class Membership_verificationAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'id_type', 'timestamp', 'verification_status', 'id_image')
admin.site.register(Membership_verification, Membership_verificationAdmin)



class Membership_RegistrationAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'surname', 'gender', 'age', 'next_of_kin', 'next_of_kin_phone', 'reg_date',
        'identification', 'occupation', 'address', 'city', 'state', 'telephone',
        'email', 'passport'  
        )
admin.site.register(Membership_Registration, Membership_RegistrationAdmin)


